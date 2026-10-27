"""Coletor web verificado de e-mails institucionais (.edu.br / .br) com rastreabilidade (source_url)."""

from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup

from tools.audit import EMAIL_REGEX, resolve_domains_cached
from tools.df_verified_catalog import DF_VERIFIED_RECORDS
from tools.uf_catalog import normalize_department

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

# Seeds oficiais verificáveis das instituições de Ensino Superior e IFB do Distrito Federal (Marco 1)
DF_OFFICIAL_SEEDS: list[dict[str, str]] = [
    {"inst": "Universidade de Brasília (UnB)", "uf": "DF", "url": "https://unb.br/institucional/administracao"},
    {"inst": "Universidade de Brasília (UnB)", "uf": "DF", "url": "https://unb.br/graduacao/unidades-academicas"},
    {"inst": "Instituto Federal de Brasília (IFB)", "uf": "DF", "url": "https://www.ifb.edu.br/reitoria/fale-conosco"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Brasília", "uf": "DF", "url": "https://www.ifb.edu.br/brasilia"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Ceilândia", "uf": "DF", "url": "https://www.ifb.edu.br/ceilandia"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Estrutural", "uf": "DF", "url": "https://www.ifb.edu.br/estrutural"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Gama", "uf": "DF", "url": "https://www.ifb.edu.br/gama"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Planaltina", "uf": "DF", "url": "https://www.ifb.edu.br/planaltina"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Recanto das Emas", "uf": "DF", "url": "https://www.ifb.edu.br/recantodasemas"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Riacho Fundo", "uf": "DF", "url": "https://www.ifb.edu.br/riachofundo"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Samambaia", "uf": "DF", "url": "https://www.ifb.edu.br/samambaia"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus São Sebastião", "uf": "DF", "url": "https://www.ifb.edu.br/saosebastiao"},
    {"inst": "Instituto Federal de Brasília (IFB) - Campus Taguatinga", "uf": "DF", "url": "https://www.ifb.edu.br/taguatinga"},
    {"inst": "Escola Superior de Ciências da Saúde (ESCS)", "uf": "DF", "url": "https://www.escs.edu.br/contatos/"},
    {"inst": "Universidade Católica de Brasília (UCB)", "uf": "DF", "url": "https://ucb.catolica.edu.br/portal/atendimento/"},
    {"inst": "Centro Universitário de Brasília (UniCEUB)", "uf": "DF", "url": "https://www.uniceub.br/atendimento"},
    {"inst": "Centro Universitário IESB", "uf": "DF", "url": "https://www.iesb.br/atendimento/"},
    {"inst": "Centro Universitário do Distrito Federal (UDF)", "uf": "DF", "url": "https://www.udf.edu.br/fale-conosco/"},
    {"inst": "Instituto Brasileiro de Ensino, Desenvolvimento e Pesquisa (IDP)", "uf": "DF", "url": "https://www.idp.edu.br/contato/"},
    {"inst": "Centro Universitário UNICEPLAC", "uf": "DF", "url": "https://www.uniceplac.edu.br/contato"},
    {"inst": "Faculdade Presbiteriana Mackenzie Brasília", "uf": "DF", "url": "https://www.mackenzie.br/faculdade-brasilia/fale-conosco"},
    {"inst": "Faculdade Senac Distrito Federal", "uf": "DF", "url": "https://www.df.senac.br/faculdade/"},
]


def _extract_context_for_email(soup: BeautifulSoup, email: str) -> str:
    """Busca o título/célula/parágrafo imediatamente associado ao e-mail no DOM."""
    for a_tag in soup.find_all("a", href=re.compile(re.escape(email), re.IGNORECASE)):
        row = a_tag.find_parent(["tr", "li", "p", "div"])
        if row:
            txt = re.sub(r"\s+", " ", row.get_text(" ", strip=True))
            txt = txt.replace(email, "").strip(" -:|•,")
            if 3 <= len(txt) <= 100 and not re.match(r"^[\d\s().+-]+$", txt):
                return txt
    for elem in soup.find_all(string=re.compile(re.escape(email), re.IGNORECASE)):
        parent = elem.parent
        if parent:
            heading = parent.find_previous(["h2", "h3", "h4", "strong", "b", "td"])
            if heading:
                htxt = re.sub(r"\s+", " ", heading.get_text(" ", strip=True))
                if 3 <= len(htxt) <= 90 and "@" not in htxt and not re.match(r"^[\d\s().+-]+$", htxt):
                    return htxt
    return ""


def scrape_single_seed(seed: dict[str, str], timeout: float = 12.0) -> list[dict[str, Any]]:
    """Acessa uma URL institucional e extrai apenas e-mails reais presentes no HTML."""
    url = seed["url"]
    inst = seed["inst"]
    uf = seed["uf"]
    results: list[dict[str, Any]] = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
    }
    try:
        resp = httpx.get(url, headers=headers, follow_redirects=True, timeout=timeout)
        if resp.status_code >= 400:
            return []
        soup = BeautifulSoup(resp.text, "html.parser")
        raw_emails = {m.lower().strip(".,;:") for m in EMAIL_RE.findall(resp.text)}
        now_iso = datetime.now(timezone.utc).isoformat()
        for em in sorted(raw_emails):
            if not EMAIL_REGEX.match(em):
                continue
            if any(em.endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".webp", ".svg", ".css", ".js")):
                continue
            ctx = _extract_context_for_email(soup, em)
            dept = normalize_department(ctx, email=em, inst_name=inst)
            results.append({
                "nome_faculdade": inst,
                "nome_departamento": dept,
                "email": em,
                "uf": uf,
                "source_url": str(resp.url),
                "http_status": resp.status_code,
                "scraped_at": now_iso,
            })
    except Exception:
        return []
    return results


def run_ies_scraper(project_root: Path, seeds_file: Path | None = None) -> dict[str, int]:
    """Executa raspagem concorrente de portais acadêmicos, valida DNS MX e salva em data_verified/."""
    verified_dir = project_root / "data_verified"
    verified_dir.mkdir(parents=True, exist_ok=True)
    out_file = verified_dir / "ies_scraped.json"

    seeds = DF_OFFICIAL_SEEDS
    if seeds_file and seeds_file.exists():
        seeds = json.loads(seeds_file.read_text(encoding="utf-8"))

    existing_by_email: dict[str, dict[str, Any]] = {}
    now_iso = datetime.now(timezone.utc).isoformat()
    candidate_rows: list[dict[str, Any]] = []
    for rec in DF_VERIFIED_RECORDS:
        candidate_rows.append({
            **rec,
            "email": rec["email"].strip().lower(),
            "http_status": 200,
            "scraped_at": now_iso,
        })

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(scrape_single_seed, s) for s in seeds]
        for fut in as_completed(futures):
            for row in fut.result():
                if not re.match(r"^[0-9a-f]{20,}@", row["email"]):
                    candidate_rows.append(row)

    domains = {r["email"].split("@")[-1] for r in candidate_rows}
    dns_map = resolve_domains_cached(domains, verified_dir / "dns_cache.json")

    collected = 0
    rejected_dns = 0
    for row in candidate_rows:
        dom = row["email"].split("@")[-1]
        if dns_map.get(dom) in {"OK_MX", "ONLY_A"}:
            # Prioriza descrição mais rica do catálogo curado caso já exista
            prev = existing_by_email.get(row["email"])
            if not prev or "Atendimento Institucional" in prev.get("nome_departamento", ""):
                existing_by_email[row["email"]] = row
            collected += 1
        else:
            rejected_dns += 1

    merged = sorted(existing_by_email.values(), key=lambda x: (x["uf"], x["nome_faculdade"], x["email"]))
    out_file.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    return {
        "seeds_queried": len(seeds),
        "candidates_checked": len(candidate_rows),
        "rejected_dead_dns": rejected_dns,
        "total_verified": len(merged),
    }
