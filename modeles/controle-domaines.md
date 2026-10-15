# Relevé local des contrôles par domaine

Créer un fichier JSON par mesure dans `candidats/<identifiant>/_travail/collectes/<session>/consolidation/controles-domaines/`. Son nom utilise l’identifiant de mesure, ou l’identifiant stable d’extraction avant création de la fiche. Le candidat et l’agent restent uniques selon la procédure.

## Structure

- `candidat`, `agent`, `session`, `mesure_id` ou `extraction_id` : rattachement sans ambiguïté.
- `date_controle` : date réelle du contrôle.
- `guides` : liste des chemins des guides chargés, dont le socle, et leur `version` affichée ; ajouter l’empreinte du fichier si elle est calculée.
- `controles` : une entrée par identifiant du socle et des guides chargés, avec les champs ci-dessous.
- `bilan` : synthèse des questions documentées, introuvables, non applicables et à compléter, avec les lacunes à publier.

Pour chaque entrée de `controles` :

| Champ | Contenu |
| --- | --- |
| `id` | Identifiant exact du contrôle, par exemple `RET-05`. |
| `question_appliquee` | Question concrète pour cette mesure, ou motif de non-applicabilité. |
| `resultat` | `documente`, `non_trouve`, `non_applicable` ou `a_completer`, selon le guide d’utilisation. |
| `reponse` | Constat factuel ou inconnue ; ne pas confondre documentation et validation de la promesse. |
| `references` | Identifiants des références communes, versions, URL originales et repères précis réellement consultés. Tableau vide si aucune référence retenue. |
| `recherches` | Producteur, publication ou requête, URL si connue, date de consultation, résultat et obstacle éventuel. |
| `limites` | Définition, comparabilité, actualité, incertitude, données absentes ou contradictoires. |
| `calculs_agent` | Entrées sourcées, formule, unités et hypothèses des calculs éventuels ; tableau vide sinon. |

Un `documente` peut constater que le candidat ne précise pas un paramètre ou que deux sources ne sont pas comparables, à condition de l’étayer. Il ne signifie pas qu’un chiffrage est correct. `non_trouve` exige des recherches réelles ; un `non_applicable` exige un motif spécifique.

## Avant l’écriture publique

Vérifier que tous les identifiants attendus sont présents une seule fois et qu’aucun n’est `a_completer`. Lier ce relevé depuis l’entrée correspondante de `recherche-independante.json` et depuis la décision de consolidation. Conserver dans la fiche publique les guides/versions, les références et les lacunes importantes, y compris celles qui limitent une conclusion. Ne pas publier un lien vers ce fichier local ignoré comme seule preuve.

Un relevé rempli par une IA est une trace de travail, pas une certification. Les règles décrivent ce que l’agent doit contrôler ; aucun validateur automatique de fond n’est fourni à ce stade.
