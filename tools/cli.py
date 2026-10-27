"""Interface de linha de comando (CLI) unificada do Projeto Edumi."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tools.audit import run_audit
from tools.etl_legacy import ingest_legacy_spreadsheets
from tools.exporter import build_deliverables
from tools.scraper_ies import run_ies_scraper
from tools.scraper_social import extract_motim_candidates, import_verified_social_batch, probe_instagram_public_meta


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="edumi",
        description="Ferramental determinístico de auditoria, ETL e coleta verificada — Projeto Edumi",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_audit = sub.add_parser("audit", help="Audita integridade, DNS MX, bounces e alucinações nas bases CSV")
    p_audit.add_argument("--dir", default="csv_exports", help="Pasta alvo (csv_exports ou data_staged)")

    sub.add_parser("ingest-legacy", help="Extrai e higieniza as 7 planilhas originais de /doc para data_staged/")

    p_ies = sub.add_parser("scrape-ies", help="Coleta e-mails reais em portais oficiais (.edu.br / .br)")
    p_ies.add_argument("--seeds", default=None, help="Arquivo JSON opcional com seeds customizados")

    p_soc = sub.add_parser("verify-social", help="Sonda perfis públicos ou importa lote social verificado")
    p_soc.add_argument("--probe", nargs="*", help="Lista de @arrobas para sondar via HTTP público")
    p_soc.add_argument("--import-json", default=None, help="Caminho de lote JSON verificado para importar")
    p_soc.add_argument("--list-motim", action="store_true", help="Lista contagem de expositores brutos da Motim")

    p_build = sub.add_parser("build", help="Compila entregáveis (.csv, .xlsx e data_payload.js) após passar no audit")
    p_build.add_argument("--no-strict", action="store_true", help="Permite gerar mesmo com avisos pendentes")

    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent

    if args.cmd == "audit":
        res = run_audit(root, target_dir=root / args.dir)
        print(json.dumps({
            "target_dir": res["target_dir"],
            "total_blockers": res["total_blockers"],
            "tables": {
                k: {
                    "rows": v["rows"],
                    "blockers": v["blockers_count"],
                    "bounces": v["bounced_emails_leaked"],
                    "dead_dns": v["dead_dns_emails"],
                    "unverified": v["unverified_or_synthetic_emails"] or v["unverified_social_handles"],
                    "dirty_depts": v["dirty_departments_count"],
                    "invalid_ufs": v["invalid_ufs"],
                }
                for k, v in res["tables"].items()
            },
        }, indent=2, ensure_ascii=False))
        sys.exit(0)

    if args.cmd == "ingest-legacy":
        stats = ingest_legacy_spreadsheets(root)
        print(json.dumps({"status": "ok", "staged_counts": stats}, indent=2, ensure_ascii=False))
        sys.exit(0)

    if args.cmd == "scrape-ies":
        seeds_path = Path(args.seeds) if args.seeds else None
        stats = run_ies_scraper(root, seeds_file=seeds_path)
        print(json.dumps({"status": "ok", **stats}, indent=2, ensure_ascii=False))
        sys.exit(0)

    if args.cmd == "verify-social":
        if args.list_motim:
            cands = extract_motim_candidates(root)
            print(json.dumps({"motim_unique_candidates": len(cands), "sample": cands[:15]}, indent=2, ensure_ascii=False))
            sys.exit(0)
        if args.probe:
            out = [probe_instagram_public_meta(h) for h in args.probe]
            print(json.dumps(out, indent=2, ensure_ascii=False))
            sys.exit(0)
        if args.import_json:
            res = import_verified_social_batch(root, Path(args.import_json))
            print(json.dumps(res, indent=2, ensure_ascii=False))
            sys.exit(0)
        p_soc.print_help()
        sys.exit(1)

    if args.cmd == "build":
        res = build_deliverables(root, strict=not args.no_strict)
        print(json.dumps({"status": "built", **res}, indent=2, ensure_ascii=False))
        sys.exit(0)


if __name__ == "__main__":
    main()
