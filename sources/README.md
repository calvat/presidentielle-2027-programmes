# Sources et données de référence

Cette base rassemble des données publiées par des organismes nationaux et internationaux compétents, indépendamment des documents des candidats. Elle fournit un contexte commun aux fiches de mesures et à leurs vérifications.

## Organisation

- `references/` : fiches de séries statistiques, indicateurs ou publications, selon `modeles/reference.md`.
- `documents/` : documents de tiers autorisés et notices de droits propres à chaque source.
- `organismes.md` : répertoire initial des producteurs à consulter, sans présumer que toutes leurs publications ont été récupérées ou vérifiées.
- [Repères par domaine](reperes-domaines.md) : points d’entrée institutionnels, utilité et état d’accès lors du repérage pour les guides. Ils ne remplacent pas les références de séries ou publications précises.

La base est initialement vide. Un organisme répertorié ne constitue pas une donnée collectée.

## Collecte

Consulter la publication d’origine et privilégier les tableaux téléchargeables, API et formats structurés lorsque disponibles. Conserver le lien précis vers la série ou le tableau, pas seulement la page d’accueil de l’organisme. Documenter l’identifiant de série, les filtres et la méthode d’extraction pour rendre la collecte reproductible.

Conserver les données d’origine lorsque leur licence le permet, dans `sources/documents/<identifiant>/`, avec une notice selon `modeles/document-source.md` et un lien depuis la référence, en indiquant leur licence et leur provenance. Sinon, conserver les liens et une fiche descriptive. Ne pas placer automatiquement ces données sous la CC0 du projet.

Commencer par les références nécessaires aux mesures documentées, puis élargir progressivement la base. Réutiliser une même référence dans plusieurs fiches plutôt que recopier des chiffres susceptibles de diverger.

## Comparabilité et entretien

Pour chaque valeur : définition, période, territoire, population, unité, prix courants ou constants, ajustements éventuels, version de publication et statut provisoire ou définitif. Une donnée indisponible reste manquante ; ne pas l’interpoler silencieusement.

Distinguer observations, estimations statistiques, prévisions et scénarios. En cas de différence entre deux organismes, examiner les définitions, méthodes et dates avant de conclure à une contradiction. Ne pas choisir le chiffre le plus favorable à un candidat.

Lors d’une révision, dater la mise à jour et identifier les mesures concernées pour réexaminer leurs comparaisons. Toute fiche de mesure utilisant un indicateur cite l’identifiant de la référence, sa version et la valeur utilisée.

## Utilisation obligatoire dans les mesures

Avant la consolidation finale, chaque mesure fait l’objet d’une recherche dans cette base, puis auprès des producteurs pertinents si les références manquent ou sont insuffisantes. Les résultats alimentent sa section « Données publiques sur le sujet » et, lorsque possible, une mise en regard avec les déclarations du candidat. Les nouvelles références sont intégrées séquentiellement pour éviter les conflits entre agents. Une recherche sans résultat pertinent est documentée ; ne pas inventer une comparaison ni assimiler le contexte à un contre-chiffrage.
