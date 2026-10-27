"""Validador e coletor de perfis reais (@edicoesmotim DF e Influenciadores DF/GO/PE)."""

from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

from bs4 import BeautifulSoup

FOLLOWER_META_RE = re.compile(
    r"([\d.,]+\s*[KkMmBb]?|\d[\d.,]*)\s*(?:Followers|seguidores)",
    flags=re.IGNORECASE,
)

UF_BIO_KEYWORDS: dict[str, tuple[str, ...]] = {
    "DF": ("brasília", "brasilia", "bsb", "distrito federal", "/df", "- df", "061", "(61)", "asa norte", "asa sul", "taguatinga", "ceilândia", "guará", "unb"),
    "GO": ("goiânia", "goiania", "goiás", "goias", "/go", "- go", "062", "(62)", "anápolis", "ufg", "puc-go"),
    "PE": ("recife", "olinda", "pernambuco", "caruaru", "petrolina", "/pe", "- pe", "081", "(81)", "ufpe", "ufrpe", "porto digital"),
}


def parse_follower_string(raw: str) -> int | None:
    """Converte strings reais de meta tag ('12,4 mil', '32.5K', '4,821') em inteiro exato."""
    s = raw.strip().upper().replace(" ", "")
    mult = 1
    if s.endswith("K"):
        mult = 1_000
        s = s[:-1]
    elif s.endswith("M"):
        mult = 1_000_000
        s = s[:-1]
    s_clean = s.replace(",", ".") if mult > 1 else re.sub(r"[.,]", "", s)
    try:
        return int(float(s_clean) * mult)
    except ValueError:
        return None


def extract_motim_candidates(project_root: Path) -> list[str]:
    """Lê os arquivos oficiais pré-selecionados da Motim (N22/N23/brutos) e desduplica nomes."""
    raw_dir = project_root / "data_raw"
    candidates: dict[str, str] = {}
    f_brutos = raw_dir / "artistas_motim_brutos.txt"
    if f_brutos.exists():
        for line in f_brutos.read_text(encoding="utf-8", errors="replace").splitlines():
            clean = line.strip()
            if clean and len(clean) >= 2:
                candidates.setdefault(clean.lower(), clean)
    return [candidates[k] for k in sorted(candidates)]


def probe_instagram_public_meta(handle: str, timeout: float = 10.0) -> dict[str, Any]:
    """Consulta a URL pública do perfil para verificar existência e extrair og:description real."""
    clean_handle = handle.strip().lstrip("@").split("/")[0]
    url = f"https://www.instagram.com/{clean_handle}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8",
    }
    try:
        resp = httpx.get(url, headers=headers, follow_redirects=True, timeout=timeout)
        if resp.status_code == 404:
            return {"exists": False, "url": url, "status": 404}
        text = html.unescape(resp.text)
        if "Page Not Found" in text or "Esta página não está disponível" in text:
            return {"exists": False, "url": url, "status": 404}

        soup = BeautifulSoup(resp.text, "html.parser")
        meta_tag = soup.find("meta", property="og:description") or soup.find("meta", attrs={"name": "description"})
        meta_desc = meta_tag.get("content", "") if meta_tag else ""

        followers = None
        if meta_desc:
            m_fol = FOLLOWER_META_RE.search(meta_desc)
            if m_fol:
                followers = parse_follower_string(m_fol.group(1))

        inferred_uf = ""
        lower_blob = text.lower()
        for uf, kws in UF_BIO_KEYWORDS.items():
            if any(kw in lower_blob for kw in kws):
                inferred_uf = uf
                break

        return {
            "exists": resp.status_code == 200,
            "url": url,
            "status": resp.status_code,
            "followers": followers,
            "og_description": meta_desc[:240],
            "uf_hint": inferred_uf,
        }
    except Exception as exc:
        return {"exists": None, "url": url, "error": str(exc)}


def import_verified_social_batch(project_root: Path, batch_path: Path) -> dict[str, int]:
    """Importa lote verificado (ex.: via Chrome DevTools / inspeção real) exigindo source_url e seguidores reais."""
    verified_dir = project_root / "data_verified"
    verified_dir.mkdir(parents=True, exist_ok=True)
    social_file = verified_dir / "social_verified.json"

    existing: dict[str, dict[str, Any]] = {}
    if social_file.exists():
        for item in json.loads(social_file.read_text(encoding="utf-8")):
            existing[f"{item['categoria']}:{item['arroba'].lower()}"] = item

    incoming = json.loads(batch_path.read_text(encoding="utf-8"))
    accepted = 0
    rejected = 0
    now_iso = datetime.now(timezone.utc).isoformat()

    for row in incoming:
        cat = (row.get("categoria") or "").strip().lower()
        arroba = (row.get("arroba") or "").strip()
        if arroba and not arroba.startswith("@"):
            arroba = "@" + arroba
        seguidores = row.get("quantidade_seguidores")
        uf = (row.get("uf") or "").strip().upper()
        source_url = (row.get("source_url") or "").strip()

        valid_cat = cat in {"artistas", "influenciadores"}
        valid_uf = (uf == "DF") if cat == "artistas" else (uf in {"DF", "GO", "PE"})
        if not (valid_cat and arroba and isinstance(seguidores, int) and seguidores > 0 and valid_uf and source_url.startswith("http")):
            rejected += 1
            continue

        existing[f"{cat}:{arroba.lower()}"] = {
            "categoria": cat,
            "nome": row["nome"].strip(),
            "arroba": arroba,
            "quantidade_seguidores": seguidores,
            "tipo": row["tipo"].strip(),
            "uf": uf,
            "source_url": source_url,
            "verified_at": row.get("verified_at") or now_iso,
        }
        accepted += 1

    social_file.write_text(json.dumps(list(existing.values()), indent=2, ensure_ascii=False), encoding="utf-8")
    return {"accepted": accepted, "rejected": rejected, "total_verified": len(existing)}
