#!/usr/bin/env python3
"""Générer sources/references/INDEX.md : références par domaine, état de revalidation et fiches qui les citent.

Sans accès réseau. Lit uniquement les en-têtes des fiches de references/ et cherche leur identifiant dans
les fiches de mesures (candidats/*/mesures/*.md). Option --verifier : signale les liens cassés et sort en erreur.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
REFS = RACINE / "sources" / "references"
CLES = ("id", "organisme", "domaines", "millesime", "statut_donnee", "date_publication",
        "date_consultation", "revalider_apres", "version")


def lire_entete(chemin):
    texte = chemin.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return None
    donnees = {}
    for ligne in m.group(1).splitlines():
        if ":" not in ligne:
            continue
        cle, valeur = ligne.split(":", 1)
        cle, valeur = cle.strip(), valeur.strip()
        if valeur.startswith("[") and valeur.endswith("]"):
            donnees[cle] = [x.strip().strip('"') for x in valeur[1:-1].split(",") if x.strip()]
        else:
            donnees[cle] = None if valeur == "null" else valeur.strip('"')
    return donnees


def fiches_citantes(identifiants):
    resultat = {i: [] for i in identifiants}
    inconnus = []
    for fiche in sorted(RACINE.glob("candidats/*/mesures/*.md")):
        texte = fiche.read_text(encoding="utf-8")
        rel = fiche.relative_to(RACINE).as_posix()
        for i in identifiants:
            if i in texte:
                resultat[i].append(rel)
        for cible in re.findall(r"sources/references/([A-Za-z0-9._-]+)\.md", texte):
            if cible not in identifiants and cible != "INDEX":
                inconnus.append((rel, cible))
    return resultat, inconnus


def etat(entete, aujourdhui):
    statut = entete.get("statut_donnee") or ""
    echeance = entete.get("revalider_apres")
    if statut == "definitive" and not echeance:
        return "stable (non recontrôlée)"
    if not echeance:
        return "échéance non renseignée"
    return "à revalider" if echeance <= aujourdhui.isoformat() else "à jour jusqu’au " + echeance


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verifier", action="store_true", help="échouer si une fiche cite une référence inexistante")
    args = parser.parse_args()
    aujourdhui = date.today()
    entetes = {}
    for chemin in sorted(REFS.glob("*.md")):
        if chemin.name == "INDEX.md":
            continue
        entete = lire_entete(chemin)
        if not entete or entete.get("id") != chemin.stem:
            print(f"En-tête invalide ou id différent du nom de fichier : {chemin.name}", file=sys.stderr)
            return 1
        entetes[chemin.stem] = entete
    citantes, inconnus = fiches_citantes(set(entetes))
    par_domaine = {}
    for identifiant, entete in entetes.items():
        for domaine in entete.get("domaines") or ["autres"]:
            par_domaine.setdefault(domaine, []).append(identifiant)
    lignes = [
        "# Index des références communes",
        "",
        "Fichier généré par `python3 scripts/indexer_references.py` ; ne pas l’éditer à la main. "
        f"Dernière génération : {aujourdhui.isoformat()}.",
        "",
        "Chaque référence est partagée par tous les candidats. Lire cet index et [`../lacunes.md`](../lacunes.md) "
        "avant toute recherche extérieure. Une référence « stable » n’est pas recontrôlée lors d’un rafraîchissement "
        "normal ; une référence « à revalider » l’est ; un rafraîchissement profond (demande explicite) recontrôle tout.",
        "",
    ]
    for domaine in sorted(par_domaine):
        lignes += [f"## {domaine}", "",
                   "| Référence | Organisme | Millésime | Statut | Consultée le | Revalidation | Fiches qui la citent |",
                   "| --- | --- | --- | --- | --- | --- | --- |"]
        for identifiant in sorted(par_domaine[domaine]):
            e = entetes[identifiant]
            citees = citantes.get(identifiant) or []
            liens = ", ".join(f"[{Path(c).parent.parent.name}/{Path(c).stem}](../../{c})" for c in citees) or "—"
            lignes.append(
                f"| [{identifiant}]({identifiant}.md) | {e.get('organisme', '')} | {e.get('millesime', '')} | "
                f"{e.get('statut_donnee', '')} | {e.get('date_consultation', '')} | {etat(e, aujourdhui)} | {liens} |")
        lignes.append("")
    (REFS / "INDEX.md").write_text("\n".join(lignes), encoding="utf-8")
    print(f"{len(entetes)} références indexées dans {len(par_domaine)} domaines.")
    for fiche, cible in inconnus:
        print(f"Lien cassé : {fiche} cite sources/references/{cible}.md", file=sys.stderr)
    return 1 if (args.verifier and inconnus) else 0


if __name__ == "__main__":
    sys.exit(main())
