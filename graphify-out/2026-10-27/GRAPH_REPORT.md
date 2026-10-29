# Graph Report - freela-edumi  (2026-10-27)

## Corpus Check
- 41 files · ~103,970 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 16 file(s) not represented in the graph (top: .csv 13, (none) 1, .ics 1)

## Summary
- 155 nodes · 278 edges · 13 communities (9 shown, 4 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d2a5ccec`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- re
- audit.py
- json
- cli.py
- exporter.py
- 2. Padrão de Schemas (5 Abas Oficiais da Gabi)
- Edumi — Centralizador de Prospecção & Engenharia de Dados
- __init__.py
- edumi-ops
- 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi
- 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi
- Relatório de Auditoria Técnica & Veracidade — Projeto Edumi

## God Nodes (most connected - your core abstractions)
1. `ingest_legacy_spreadsheets()` - 16 edges
2. `run_audit()` - 14 edges
3. `build_deliverables()` - 13 edges
4. `main()` - 11 edges
5. `resolve_domains_cached()` - 10 edges
6. `run_ies_scraper()` - 9 edges
7. `load_legacy_emails_and_bounces()` - 8 edges
8. `probe_instagram_public_meta()` - 8 edges
9. `normalize_department()` - 8 edges
10. `Edumi — Centralizador de Prospecção & Engenharia de Dados` - 8 edges

## Surprising Connections (you probably didn't know these)
- `ingest_legacy_spreadsheets()` --calls--> `load_legacy_emails_and_bounces()`  [EXTRACTED]
  tools/etl_legacy.py → tools/audit.py
- `ingest_legacy_spreadsheets()` --calls--> `resolve_domains_cached()`  [EXTRACTED]
  tools/etl_legacy.py → tools/audit.py
- `run_ies_scraper()` --calls--> `resolve_domains_cached()`  [EXTRACTED]
  tools/scraper_ies.py → tools/audit.py
- `main()` --calls--> `run_audit()`  [EXTRACTED]
  tools/cli.py → tools/audit.py
- `build_deliverables()` --calls--> `run_audit()`  [EXTRACTED]
  tools/exporter.py → tools/audit.py

## Import Cycles
- None detected.

## Communities (13 total, 4 thin omitted)

### Community 0 - "re"
Cohesion: 0.16
Nodes (3): _extract_context_for_email(), scrape_single_seed(), normalize_department()

### Community 1 - "audit.py"
Cohesion: 0.10
Nodes (8): clean_institution_name(), clean_phone(), ingest_legacy_spreadsheets(), upsert_uni(), split_valid_emails(), build_deliverables(), classify_institution_type(), resolve_uf()

### Community 2 - "json"
Cohesion: 0.19
Nodes (3): get_existing_column(), main(), build_full_quarantine_report()

### Community 3 - "cli.py"
Cohesion: 0.14
Nodes (6): main(), run_ies_scraper(), extract_motim_candidates(), import_verified_social_batch(), parse_follower_string(), probe_instagram_public_meta()

### Community 4 - "exporter.py"
Cohesion: 0.16
Nodes (6): check_domain_dns(), detect_synthetic_followers(), load_legacy_emails_and_bounces(), mask_if_personal(), resolve_domains_cached(), run_audit()

### Community 5 - "2. Padrão de Schemas (5 Abas Oficiais da Gabi)"
Cohesion: 0.12
Nodes (16): 1. Visão Geral e Contexto Operacional, 2. Padrão de Schemas (5 Abas Oficiais da Gabi), 3. Cronograma Executivo e Status Real dos Marcos, 4. Comandos da Esteira de Engenharia (`edumi-ops`), 5. Procedimento de Segurança para Descarte das Bases Antigas, Aba 1: `universidades`, Aba 2: `artistas`, Aba 3: `influenciadores` (+8 more)

### Community 6 - "Edumi — Centralizador de Prospecção & Engenharia de Dados"
Cohesion: 0.22
Nodes (8): 🖥️ Aplicações Web Locais (`app.html` & `dashboard.html`), 🛠️ CLI de Operação e Auditoria (`uv`), 📅 Cronograma de Entregas (Milestones), Edumi — Centralizador de Prospecção & Engenharia de Dados, 📊 Estrutura Atual Auditada (5 Abas Oficiais), 📁 Estrutura de Diretórios, 🎯 Objetivo do Projeto, 🔒 Segurança, Governança e Quarentena

### Community 10 - "🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi"
Cohesion: 0.33
Nodes (5): 1. Princípio de Não-Destruição e Segurança, 2. Resumo Quantitativo por Categoria, 3. Tabela Completa de Itens Retirados, 4. Como Reativar um Contato se Necessário, 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi

### Community 11 - "🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi"
Cohesion: 0.33
Nodes (5): 1. Princípio de Não-Destruição e Segurança, 2. Resumo Quantitativo por Categoria, 3. Tabela Completa de Itens Retirados, 4. Como Reativar um Contato se Necessário, 🛡️ Relatório Oficial de Itens Expurgados e Base em Quarentena — Projeto Edumi

## Knowledge Gaps
- **1 isolated node(s):** `edumi-ops`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 83 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ingest_legacy_spreadsheets()` connect `audit.py` to `re`, `json`, `cli.py`, `exporter.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **What connects `edumi-ops` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `audit.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09879032258064516 - nodes in this community are weakly interconnected._
- **Why does `build_deliverables()` connect `audit.py` to `json`, `cli.py`, `exporter.py`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Should `cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13852813852813853 - nodes in this community are weakly interconnected._
- **Why does `run_audit()` connect `exporter.py` to `audit.py`, `json`, `cli.py`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Should `2. Padrão de Schemas (5 Abas Oficiais da Gabi)` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._