#!/usr/bin/env python3
"""Détecter les sources d'un candidat qui ont changé depuis le dernier contrôle.

Lit candidats/<identifiant>/suivi-sources.json (registre public : URL, empreinte, dernier contrôle), récupère
chaque URL et classe : inchangee, modifiee, nouvelle (pas d'empreinte de référence), inaccessible.
N'écrit dans le registre qu'avec --ecrire. Dépendances : bibliothèque standard uniquement.

Limites : l'empreinte d'une page HTML porte sur son texte visible normalisé (balises de navigation, scripts et
styles écartés) ; elle peut changer sans modification de fond ou rester identique si le contenu est chargé
dynamiquement. Un PDF est comparé par ses en-têtes (ETag, Last-Modified) lorsqu'ils existent, sinon par ses octets.
L'absence de changement détectée n'est pas une preuve d'identité du contenu.
"""
import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

RACINE = Path(__file__).resolve().parents[1]
AGENT = "presidentielle-2027-programmes/verifier_sources (collecte documentaire)"
IGNORES = {"script", "style", "noscript", "nav", "header", "footer", "form", "svg", "template"}
TAILLE_MAX = 60 * 1024 * 1024


class Texte(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.profondeur_ignoree = 0
        self.morceaux = []

    def handle_starttag(self, balise, attrs):
        if balise in IGNORES:
            self.profondeur_ignoree += 1

    def handle_endtag(self, balise):
        if balise in IGNORES and self.profondeur_ignoree:
            self.profondeur_ignoree -= 1

    def handle_data(self, donnees):
        if not self.profondeur_ignoree:
            self.morceaux.append(donnees)


def texte_normalise(octets, encodage):
    parseur = Texte()
    parseur.feed(octets.decode(encodage or "utf-8", errors="replace"))
    return re.sub(r"\s+", " ", " ".join(parseur.morceaux)).strip()


def recuperer(source):
    requete = urllib.request.Request(source["url"], headers={"User-Agent": AGENT})
    if source.get("etag"):
        requete.add_header("If-None-Match", source["etag"])
    elif source.get("last_modified"):
        requete.add_header("If-Modified-Since", source["last_modified"])
    try:
        with urllib.request.urlopen(requete, timeout=40) as reponse:
            entetes = reponse.headers
            octets = reponse.read(TAILLE_MAX + 1)
            if len(octets) > TAILLE_MAX:
                return {"erreur": "document trop volumineux"}
            type_contenu = entetes.get("Content-Type", "")
            if "html" in type_contenu or source.get("type") == "html":
                empreinte = hashlib.sha256(texte_normalise(octets, entetes.get_content_charset()).encode()).hexdigest()
                nature = "texte"
            else:
                empreinte = hashlib.sha256(octets).hexdigest()
                nature = "octets"
            return {"empreinte": empreinte, "nature": nature, "etag": entetes.get("ETag"),
                    "last_modified": entetes.get("Last-Modified"), "url_finale": reponse.geturl()}
    except urllib.error.HTTPError as e:
        if e.code == 304:
            return {"inchange_http": True}
        return {"erreur": f"HTTP {e.code}"}
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return {"erreur": str(e)}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("candidat")
    parser.add_argument("--ecrire", action="store_true", help="enregistrer empreintes et dates dans le registre")
    parser.add_argument("--ajouter", metavar="URL", action="append", default=[],
                        help="ajouter une URL au registre (sans empreinte : statut « nouvelle »)")
    parser.add_argument("--type", default="html", choices=["html", "pdf"], help="type des URL ajoutées")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.candidat):
        parser.error("Identifiant invalide.")
    chemin = RACINE / "candidats" / args.candidat / "suivi-sources.json"
    if chemin.exists():
        registre = json.loads(chemin.read_text(encoding="utf-8"))
    elif (RACINE / "candidats" / args.candidat / "README.md").is_file():
        registre = {"schema_version": 1, "candidat": args.candidat, "sources": []}
    else:
        parser.error("Dossier candidat inconnu.")
    connues = {s["url"] for s in registre["sources"]}
    for url in args.ajouter:
        if url not in connues:
            registre["sources"].append({"url": url, "type": args.type, "titre": None, "empreinte": None,
                                        "etag": None, "last_modified": None, "dernier_controle": None})
    maintenant = datetime.now(ZoneInfo("Europe/Paris")).date().isoformat()
    bilan = {"inchangee": 0, "modifiee": 0, "nouvelle": 0, "inaccessible": 0}
    for source in registre["sources"]:
        r = recuperer(source)
        if r.get("erreur"):
            statut = "inaccessible"
        elif r.get("inchange_http"):
            statut = "inchangee"
        elif not source.get("empreinte"):
            statut = "nouvelle"
        else:
            statut = "inchangee" if r["empreinte"] == source["empreinte"] else "modifiee"
        bilan[statut] += 1
        print(f"{statut:13} {source['url']}" + (f"  ({r['erreur']})" if r.get("erreur") else ""))
        if args.ecrire and statut != "inaccessible":
            source["dernier_controle"] = maintenant
            if statut != "inchangee" or "inchange_http" not in r:
                for cle in ("empreinte", "etag", "last_modified"):
                    if r.get(cle) is not None:
                        source[cle] = r[cle]
                source["nature_empreinte"] = r.get("nature", source.get("nature_empreinte"))
    print(json.dumps(bilan, ensure_ascii=False))
    if args.ecrire or args.ajouter:
        chemin.write_text(json.dumps(registre, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Registre écrit : {chemin.relative_to(RACINE)}")
    else:
        print("Registre non modifié (utiliser --ecrire après examen).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
