# Graph Report - freela-edumi  (2026-10-27)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 95 nodes · 199 edges · 9 communities (4 shown, 5 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d64e55aa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- re
- audit.py
- scraper_ies.py
- cli.py
- exporter.py
- scraper_social.py
- data_payload.js
- edumi-ops

## God Nodes (most connected - your core abstractions)
1. `ingest_legacy_spreadsheets()` - 16 edges
2. `run_audit()` - 14 edges
3. `build_deliverables()` - 13 edges
4. `main()` - 11 edges
5. `resolve_domains_cached()` - 10 edges
6. `run_ies_scraper()` - 9 edges
7. `probe_instagram_public_meta()` - 9 edges
8. `load_legacy_emails_and_bounces()` - 8 edges
9. `normalize_department()` - 8 edges
10. `scrape_single_seed()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `ingest_legacy_spreadsheets()`  [EXTRACTED]
  tools/cli.py → tools/etl_legacy.py
- `ingest_legacy_spreadsheets()` --calls--> `resolve_domains_cached()`  [EXTRACTED]
  tools/etl_legacy.py → tools/audit.py
- `ingest_legacy_spreadsheets()` --calls--> `normalize_department()`  [EXTRACTED]
  tools/etl_legacy.py → tools/uf_catalog.py
- `upsert_uni()` --calls--> `normalize_department()`  [EXTRACTED]
  tools/etl_legacy.py → tools/uf_catalog.py
- `run_ies_scraper()` --calls--> `resolve_domains_cached()`  [EXTRACTED]
  tools/scraper_ies.py → tools/audit.py

## Import Cycles
- None detected.

## Communities (9 total, 5 thin omitted)

### Community 0 - "re"
Cohesion: 0.18
Nodes (7): load_legacy_emails_and_bounces(), clean_institution_name(), clean_phone(), ingest_legacy_spreadsheets(), upsert_uni(), split_valid_emails(), resolve_uf()

### Community 1 - "audit.py"
Cohesion: 0.16
Nodes (5): check_domain_dns(), detect_synthetic_followers(), mask_if_personal(), resolve_domains_cached(), run_audit()

### Community 2 - "scraper_ies.py"
Cohesion: 0.16
Nodes (3): _extract_context_for_email(), scrape_single_seed(), normalize_department()

### Community 3 - "cli.py"
Cohesion: 0.24
Nodes (4): main(), run_ies_scraper(), extract_motim_candidates(), import_verified_social_batch()

## Knowledge Gaps
- **1 isolated node(s):** `edumi-ops`
  These have ≤1 connection - possible missing edges. (Counts symbols only; 47 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_deliverables()` connect `exporter.py` to `re`, `audit.py`, `cli.py`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **What connects `edumi-ops` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `ingest_legacy_spreadsheets()` connect `re` to `audit.py`, `scraper_ies.py`, `cli.py`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `run_audit()` connect `audit.py` to `re`, `cli.py`, `exporter.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._