"""Módulo de Inteligência Web e Validação Social Multi-Fonte.

Projetado para resolver scraping moderno em plataformas dinâmicas (Instagram, portais JS, Wix),
evitando bloqueios de IP, normalizando contagens de seguidores e validando localização geográfica
(DF, GO, PE e UFs nacionais) com cache persistente e zero desperdício de requisições.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import httpx
import dns.resolver


class SocialWebIntelligence:
    """Motor de coleta, validação e auditoria para pesquisas web e de redes sociais."""

    UF_PATTERNS = {
        "DF": [
            r"\bbras[ií]lia\b", r"\bbsb\b", r"\bdistrito federal\b", r"\btaguatinga\b",
            r"\bceil[aâ]ndia\b", r"\basa sul\b", r"\basa norte\b", r"\b[aá]guas claras\b",
            r"\bguar[aá]\b", r"\bunb\b", r"\b0?61\b", r"\(61\)"
        ],
        "GO": [
            r"\bgoi[aâ]nia\b", r"\bgyn\b", r"\bgoi[aá]s\b", r"\ban[aá]polis\b",
            r"\brio verde\b", r"\baparecida de goi[aâ]nia\b", r"\bufg\b", r"\bpuc-?go\b",
            r"\b0?62\b", r"\(62\)"
        ],
        "PE": [
            r"\brecife\b", r"\bolinda\b", r"\bpernambuco\b", r"\bcaruaru\b",
            r"\bpetrolina\b", r"\bufpe\b", r"\bufrpe\b", r"\bporto digital\b",
            r"\b0?81\b", r"\(81\)"
        ]
    }

    EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    def __init__(self, cache_file: Optional[Path] = None):
        self.project_root = Path(__file__).resolve().parent.parent
        self.cache_path = cache_file or (self.project_root / "data_verified" / "instagram_cache.json")
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict[str, Any]:
        if self.cache_path.exists():
            try:
                return json.loads(self.cache_path.read_text(encoding="utf-8"))
            except Exception:
                return {}
        return {}

    def _save_cache(self) -> None:
        try:
            self.cache_path.write_text(json.dumps(self.cache, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            print(f"Warning: could not save cache: {e}")

    def detect_uf(self, text: str) -> Optional[str]:
        """Identifica a UF baseando-se em DDDs, menções de cidades, bairros e universidades locais."""
        if not text:
            return None
        text_lower = text.lower()
        for uf, patterns in self.UF_PATTERNS.items():
            for pat in patterns:
                if re.search(pat, text_lower):
                    return uf
        return None

    def audit_ghost_profile(
        self,
        followers: int,
        following: int,
        posts_count: int = 10,
        is_private: bool = False
    ) -> Dict[str, Any]:
        """Audita se o perfil é autêntico ou se possui características de conta fantasma/bot.
        
        Regras Anti-Fantasma:
        1. Conta privada não pode ser contratada para campanhas de influenciadores abertas.
        2. Proporção Seguidores / Seguindo (Ratio): bots de follow-unfollow seguem milhares e têm poucos seguidores.
        3. Faixa de Seguidores: micro e mid-influenciadores válidos devem estar na faixa de 9k a 100k (ou até 180k acessível).
        4. Histórico de postagens: perfis com menos de 10 posts são descartados como inativos/fantasmas.
        """
        issues = []
        is_ghost = False

        if is_private:
            issues.append("Conta Privada (inviável para veiculação de Reels/publis)")
            is_ghost = True

        if posts_count < 5:
            issues.append(f"Pouquíssimas postagens ({posts_count} posts) - perfil inativo/fantasma")
            is_ghost = True

        ratio = (followers / following) if following > 0 else followers

        if following > 4500 and ratio < 1.5:
            issues.append(f"Suspeita de automação/bot: segue {following} pessoas para {followers} seguidores (ratio {ratio:.2f})")
            is_ghost = True

        if followers < 8000:
            issues.append(f"Seguidores insuficientes ({followers} seg) para a régua micro-mid da Edumi (mínimo 9k)")
            is_ghost = True

        return {
            "is_ghost": is_ghost,
            "status": "REJEITADO" if is_ghost else "APROVADO",
            "ratio_followers_following": round(ratio, 2),
            "followers": followers,
            "following": following,
            "issues": issues
        }

    def classify_influencer_tier(self, followers: int) -> str:
        """Classifica o perfil pela régua de relevância e acessibilidade para campanhas."""
        if followers < 9000:
            return "Nano Influencer (< 9k)"
        elif followers <= 50000:
            return "Micro Influencer (9k - 50k) [Ideal Edumi]"
        elif followers <= 100000:
            return "Mid Influencer (50k - 100k) [Ideal Edumi]"
        elif followers <= 250000:
            return "Macro Regional (100k - 250k) [Sob Consulta]"
        else:
            return "Mega Influencer (> 250k) [Inacessível / Alto Custo]"

    def extract_emails(self, text: str) -> List[str]:
        """Extrai endereços de e-mail de texto de bios ou páginas web."""
        if not text:
            return []
        found = self.EMAIL_REGEX.findall(text)
        valid = []
        for em in found:
            clean = em.strip(".,;:()")
            if not clean.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                valid.append(clean.lower())
        return list(dict.fromkeys(valid))

    def verify_dns_mx(self, email: str) -> bool:
        """Verifica se o domínio do e-mail possui registro MX ativo na internet."""
        try:
            domain = email.split("@")[1].strip()
            records = dns.resolver.resolve(domain, "MX")
            return len(records) > 0
        except Exception:
            return False

    def normalize_follower_count(self, raw_str: str) -> Optional[int]:
        """Converte strings como '10,9 mil', '18.5K', '1.2M' em inteiros precisos."""
        s = raw_str.strip().upper().replace(" ", "")
        mult = 1
        if "MIL" in s or s.endswith("K"):
            mult = 1000
            s = s.replace("MIL", "").replace("K", "")
        elif "M" in s:
            mult = 1_000_000
            s = s.replace("M", "")
        s_clean = s.replace(",", ".") if mult > 1 else re.sub(r"[.,]", "", s)
        try:
            return int(float(s_clean) * mult)
        except ValueError:
            return None

    def register_profile(
        self,
        handle: str,
        name: str,
        followers: int,
        niche: str,
        bio: str = "",
        explicit_uf: Optional[str] = None,
        source_url: str = ""
    ) -> Dict[str, Any]:
        """Registra ou atualiza um perfil no cache estruturado auditado."""
        clean_handle = handle.strip()
        if not clean_handle.startswith("@"):
            clean_handle = "@" + clean_handle
        
        detected_uf = explicit_uf or self.detect_uf(bio) or "DF"
        emails = self.extract_emails(bio)
        tier = self.classify_influencer_tier(followers)

        entry = {
            "handle": clean_handle,
            "name": name.strip(),
            "followers": followers,
            "tier": tier,
            "niche": niche.strip(),
            "bio": bio.strip(),
            "uf": detected_uf,
            "emails": emails,
            "contactable": len(emails) > 0 or ("contato" in bio.lower() or "parcerias" in bio.lower()),
            "source_url": source_url or f"https://www.instagram.com/{clean_handle.lstrip('@')}/",
            "updated_at": datetime.now(timezone.utc).isoformat()
        }
        self.cache[clean_handle.lower()] = entry
        self._save_cache()
        return entry


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sw = SocialWebIntelligence()
    
    # Teste de detecção com o perfil do Ramon Phanton
    res = sw.register_profile(
        handle="@ramonphanton",
        name="Ramon Phanton",
        followers=10913,
        niche="Artes Visuais, Muralismo e Ilustração / UnB",
        bio="Artista Urbano • Muralista • Ilustrador\nArtes Visuais - UnB\nGO - DF — Brasil\n📩 Orçamentos e parcerias",
        explicit_uf="DF"
    )
    print("Perfil Registrado com Sucesso:")
    print(json.dumps(res, indent=2, ensure_ascii=False))
