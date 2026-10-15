#!/usr/bin/env python3
"""Créer une session locale de collecte sans accès réseau ni écrasement."""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidat", help="Identifiant du dossier dans candidats/")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.candidat):
        parser.error("Identifiant invalide : utiliser des lettres minuscules, chiffres et tirets.")
    racine = Path(__file__).resolve().parents[1]
    candidat = racine / "candidats" / args.candidat
    if candidat.is_symlink() or not (candidat / "README.md").is_file():
        parser.error("Dossier candidat absent ou invalide ; créer d’abord son README.")
    travail = candidat / "_travail"
    collectes = travail / "collectes"
    if travail.is_symlink() or collectes.is_symlink():
        parser.error("Le répertoire de travail ne doit pas être un lien symbolique.")
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    identifiant = maintenant.strftime("%Y%m%dT%H%M%S-%f%z")
    session = collectes / identifiant
    session.mkdir(parents=True, exist_ok=False)
    for nom in ("brut", "extractions", "consolidation"):
        (session / nom).mkdir()
    manifeste = {
        "schema_version": 1,
        "candidat": args.candidat,
        "session": identifiant,
        "cree_le": maintenant.isoformat(),
        "agent_responsable": None,
        "agents": [],
        "fichiers_modifies": [],
        "etat_collecte": "non_commencee",
        "etat_recherche_independante": "non_commencee",
        "bilans_recherche_independante": [],
        "etat_consolidation": "non_commencee",
        "perimetre": [],
        "sources": [],
        "fichiers_collecte": [],
        "lacunes": [],
    }
    (session / "manifest.json").write_text(
        json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(session)


if __name__ == "__main__":
    main()
