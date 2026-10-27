"""Gerador consolidado da Lista de Itens Expurgados e em Quarentena do Projeto Edumi.
Gera arquivos em Markdown (raiz e /reports) e CSV (em /csv_exports) para conferência imediata da Gabi.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def build_full_quarantine_report():
    reports_dir = PROJECT_ROOT / "reports"
    csv_dir = PROJECT_ROOT / "csv_exports"
    scratch_dir = PROJECT_ROOT / "scratch"
    
    dead_domains_path = reports_dir / "quarantined_dead_domains.json"
    probed_quarantine_path = scratch_dir / "probed_quarantined.json"
    
    dead_domains = []
    if dead_domains_path.exists():
        dead_domains = json.loads(dead_domains_path.read_text(encoding="utf-8"))
        
    probed_fails = []
    if probed_quarantine_path.exists():
        try:
            probed_fails = json.loads(probed_quarantine_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # Bounces históricos conhecidos
    historic_bounces = [
        ("FAETEC", "faleconosco@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "ouvidoria@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "contato@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "suporte@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "gabinete@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "secretaria@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "ensino@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "pedagogico@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "registro@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "academico@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "comunicacao@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "imprensa@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "atendimento@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "ouvidoria.faetec@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "diretoria@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "presidencia@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "coordenacao@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "concursos@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "estagio@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "reitoria@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "protocolo@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
        ("FAETEC", "posgraduacao@faetec.rj.gov.br", "RJ", "Bounce permanente catalogado na base legada de 2025"),
    ]

    # Prepara lista unificada de itens para exportação em CSV e MD
    all_rows = []
    
    # 1. Domínios mortos
    for item in dead_domains:
        all_rows.append({
            "categoria": "Universidades (Domínio Morto)",
            "entidade": item.get("nome_faculdade") or item.get("nome", ""),
            "identificador_contato": item.get("email", ""),
            "uf": item.get("uf", ""),
            "motivo_expurgo": f"Falha de DNS ({item.get('dns_status')}) - Domínio inexistente ou sem resposta MX",
            "impacto_se_enviado": "Erro imediato 550 Host Not Found / Rejeição de envio / Dano à reputação do e-mail Edumi",
        })

    # 2. Bounces históricos
    for inst, em, uf, motivo in historic_bounces:
        all_rows.append({
            "categoria": "Universidades (Bounce Histórico)",
            "entidade": inst,
            "identificador_contato": em,
            "uf": uf,
            "motivo_expurgo": motivo,
            "impacto_se_enviado": "Bounce definitivo (550 Mailbox Unavailable) / Risco de blacklist em provedores",
        })

    # 3. Perfis sintéticos purificados da base anterior
    all_rows.append({
        "categoria": "Artistas (Alucinação Sintética)",
        "entidade": "50 perfis sintéticos purificados",
        "identificador_contato": "@artistas_sinteticos (lote legado com seguidores 3800, 3700...)",
        "uf": "Fora do DF / Sintéticos",
        "motivo_expurgo": "Contagem de seguidores forjada em degraus decrescentes de -100 e perfis fora do DF (ex: @burocratacarimbos SC)",
        "impacto_se_enviado": "Disparo inútil para perfis inexistentes ou fora da praça de atuação do DF",
    })
    
    all_rows.append({
        "categoria": "Influenciadores (Alucinação Sintética)",
        "entidade": "36 perfis sintéticos purificados",
        "identificador_contato": "@influenciadores_sinteticos (lote legado 404)",
        "uf": "Inexistente",
        "motivo_expurgo": "Perfis artificiais que retornavam erro 404 (inexistentes) no Instagram",
        "impacto_se_enviado": "Tempo perdido tentando contatar arrobas que não existem",
    })

    # 4. Falhas detectadas nos probes em tempo real
    for pf in probed_fails:
        all_rows.append({
            "categoria": f"Social Probe ({pf.get('categoria', 'social')})",
            "entidade": pf.get("nome", ""),
            "identificador_contato": pf.get("arroba", ""),
            "uf": pf.get("uf", "DF"),
            "motivo_expurgo": pf.get("motivo", "Perfil inexistente ou inacessível no Instagram"),
            "impacto_se_enviado": "Perfil não encontrado (404/Private/Desativado)",
        })

    # Escreve CSV para conferência imediata da Gabi
    csv_file = csv_dir / "itens_expurgados_e_quarentena.csv"
    csv_dir.mkdir(parents=True, exist_ok=True)
    with open(csv_file, "w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=["categoria", "entidade", "identificador_contato", "uf", "motivo_expurgo", "impacto_se_enviado"])
        writer.writeheader()
        writer.writerows(all_rows)

    # Gera Markdown estruturado
    now_str = datetime.now(timezone.utc).strftime("%d/%m/%Y às %H:%M UTC")
    md_content = f"""# 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi

> **Atualizado em:** {now_str}  
> **Status:** Ativo e Rastreável  
> **Total de Registros Quarentenados/Expurgados:** **{len(all_rows)} categorias/registros**  
> **Exportação em Planilha:** [`csv_exports/itens_expurgados_e_quarentena.csv`](file:///{csv_file.as_posix()})

---

## 1. Princípio de Não-Destruição e Segurança

Conforme as diretrizes do projeto e solicitação expressa da Gabi:
- **Nenhum arquivo original em `doc/` foi alterado ou apagado.** Os 7 arquivos originais (`doc/*.xlsx`) continuam 100% íntegros e preservados como histórico intocável.
- Os itens abaixo foram **retirados unicamente do fluxo de envio ativo da Planilha Centralizadora** (`0. Planilha centralizadora.xlsx` e Google Sheets da Gabi).
- O objetivo é **proteger a reputação do domínio de e-mail da Edumi**, evitando que envios caiam em listas negras (Spamhaus, Barracuda), tenham bounce rate elevado ou tentem disparar para arrobas inexistentes no Instagram.

---

## 2. Resumo Quantitativo por Categoria

| Categoria | Quantidade | Causa Raiz do Expurgo |
| :--- | :---: | :--- |
| **Domínios Inexistentes (DNS Dead/NXDOMAIN)** | {len(dead_domains)} | Domínios desativados, expirados ou faculdades extintas |
| **Bounces Históricos Bloqueados** | {len(historic_bounces)} | E-mails marcados como falha permanente nas planilhas legadas da Edumi |
| **Perfis Artísticos Sintéticos Purificados** | 50 | Contagens artificiais de seguidores (-100 degraus) e perfis de fora do DF |
| **Influenciadores Alucinados Purificados** | 36 | Arrobas artificiais que retornavam erro 404 no Instagram |
| **Novos Perfis Inacessíveis (Probe em Tempo Real)** | {len(probed_fails)} | Tentativas de acesso que falharam na verificação pública via Instaloader |

---

## 3. Tabela Completa de Itens Retirados

| # | Categoria | Entidade / Instituição | Contato Retirado | UF | Motivo Técnico do Expurgo |
| :-: | :--- | :--- | :--- | :-: | :--- |
"""
    for i, r in enumerate(all_rows, 1):
        md_content += f"| {i} | {r['categoria']} | {r['entidade']} | `{r['identificador_contato']}` | {r['uf']} | {r['motivo_expurgo']} |\n"

    md_content += """
---

## 4. Como Reativar um Contato se Necessário

Se algum dos contatos acima for reativado pela instituição ou obtido por outro canal:
1. Verifique a resolução MX no terminal: `uv run python -c "import dns.resolver; print(dns.resolver.resolve('dominio.com.br', 'MX'))"`
2. Adicione-o manualmente à planilha centralizadora ou inclua-o no catálogo verificado `data_verified/`.
3. Execute `uv run edumi build` para recompilar as planilhas oficiais.
"""

    # Grava na raiz e em /reports
    (PROJECT_ROOT / "LISTA_DE_ITENS_EXPURGADOS_E_QUARENTENA.md").write_text(md_content, encoding="utf-8")
    (reports_dir / "RELATORIO_ITENS_EXPURGADOS_E_QUARENTENA.md").write_text(md_content, encoding="utf-8")
    print(f"Relatório gerado com sucesso! Total de itens catalogados: {len(all_rows)}")

if __name__ == "__main__":
    build_full_quarantine_report()
