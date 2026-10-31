"""Módulo de filtragem departamental estrita baseado nas regras oficiais da Gabi (aba LIMPEZAS)."""

from __future__ import annotations

import re
from typing import Any

REMOVE_DEPT_KEYWORDS: list[str] = [
    "ouvidoria",
    "decanato",
    "secretaria geral",
    "secretaria acadêmica geral",
    "secretaria academica geral",
    "financeiro",
    "comercial",
    "vendas",
    "sales",
    "teleatendimento",
    "reitoria",
    "pró-reitoria",
    "pro-reitoria",
    "próreitoria",
    "tesouraria",
    "suporte",
    "suportes",
    "suportes de centrais",
    "biblioteca central",
    "central",
    "centrais",
    "central de atendimento",
    "central do aluno",
    "central de relacionamento",
    "centrais de atendimento",
    "fale conosco",
    "processo seletivo",
    "vestibular",
    "protocolo",
    "webmaster",
    "atendimento institucional",
    "atendimento geral",
    "atendimento acadêmico",
    "atendimento academico",
    "atendimento ao aluno",
    "atendimento ao estudante",
    "atendimento acadêmico-financeiro",
    "comunicação social",
    "comunicação institucional",
    "assessoria de comunicação",
    "assessoria de imprensa",
    "ascom",
    "diretório central dos estudantes",
    "diretorio central dos estudantes",
]

REMOVE_EMAIL_PREFIXES: list[str] = [
    "ouvidoria@",
    "reitoria@",
    "secretaria.reitoria@",
    "gabinete.reitoria@",
    "gabinete@",
    "financeiro@",
    "comercial@",
    "vendas@",
    "sales@",
    "contato@",
    "faleconosco@",
    "fale.conosco@",
    "atendimento@",
    "atende@",
    "protocolo@",
    "webmaster@",
    "portal@",
    "comunicacao@",
    "ascom@",
    "imprensa@",
    "tesouraria@",
    "decanato@",
    "sac@",
    "central@",
    "central.",
    "relacionamento@",
    "marketing@",
    "teleatendimento@",
    "suporte@",
    "dceunb@",
]

DESCRIPTION_INDICATORS: list[str] = [
    "forte atuação",
    "forte aderência",
    "forte ligação",
    "forte público",
    "excelente alcance",
    "excelente polo",
    "grande capilaridade",
    "grande complexo",
    "altíssima concentração",
    "ideal para",
    "presença em mais de",
    "capacitação tecnológica",
    "formação técnica em artes e cultura",
    "atuação regional",
    "atendimento e bolsas regionais",
]

PRO_REITORIA_RE = re.compile(
    r"\b(PREN|PREX|PRPI|PRAF|PROGRAD|PROPP|PROEC|PRACE|PROAE|PRPPG|PROPPI|PROPEG)\b",
    re.IGNORECASE,
)

DEPT_SPECIFIC_WORDS = [
    "departamento",
    "coordenação",
    "curso",
    "instituto",
    "faculdade",
    "programa",
    "núcleo",
    "laboratório",
    "câmpus",
    "campus",
    "centro de",
]


def is_description_not_dept(dept: str) -> bool:
    d = dept.lower().strip()
    if d.endswith(".") and len(d) > 30:
        return True
    return any(indicator in d for indicator in DESCRIPTION_INDICATORS)


def is_clean_departmental_contact(row: dict[str, Any]) -> bool:
    dept = (row.get("nome_departamento") or "").strip()
    email = (row.get("email") or "").strip().lower()
    fac = (row.get("nome_faculdade") or "").strip().lower()

    dept_lower = dept.lower()

    # 1) Palavras-chave de setores centrais no departamento
    for kw in REMOVE_DEPT_KEYWORDS:
        if kw in dept_lower:
            if "secretaria geral" in kw and "secretaria do departamento" in dept_lower:
                continue
            if "reitoria" in kw and "departamento" in dept_lower:
                continue
            return False

    # 2) Prefixo de email proibido ou genérico
    STRICT_BANNED_EMAIL_PREFIXES = (
        "ouvidoria@", "reitoria@", "secretaria.reitoria@", "gabinete.reitoria@",
        "financeiro@", "comercial@", "vendas@", "sales@", "teleatendimento@",
        "tesouraria@", "decanato@", "sac@", "suporte@", "atendimento@", "atende@",
        "central@", "central.", "relacionamento@", "marketing@", "dceunb@", "faleconosco@"
    )
    for bp in STRICT_BANNED_EMAIL_PREFIXES:
        if email.startswith(bp):
            return False

    for prefix in REMOVE_EMAIL_PREFIXES:
        if email.startswith(prefix):
            if any(w in dept_lower for w in DEPT_SPECIFIC_WORDS):
                continue
            return False

    # 3) Descrições narrativas no lugar de nomes de departamentos
    if is_description_not_dept(dept):
        return False

    # 4) "Instituição Acadêmica" genérica sem departamento específico
    if fac == "instituição acadêmica":
        if not any(w in dept_lower for w in DEPT_SPECIFIC_WORDS):
            return False

    # 5) Pró-reitorias por sigla
    if PRO_REITORIA_RE.search(dept):
        return False

    return True
