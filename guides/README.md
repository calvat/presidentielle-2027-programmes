# Guides de vérification par domaine

Version initiale : 2026-10-15. Ces 22 guides aident les agents à rechercher les éléments qu’une collecte de programme peut omettre. Ils s’appuient sur un [repérage des thèmes de 2017 et 2022](reperage-2017-2022.md), puis sur un découpage adapté aux vérifications. Ils ne constituent ni un classement des enjeux ni une garantie d’exhaustivité.

## Utilisation obligatoire avant consolidation

1. Lire le [socle commun](socle-commun.md).
2. Choisir dans la table le domaine principal et les domaines secondaires réellement concernés. Charger seulement leurs guides. Tout coût ou financement public annoncé déclenche aussi le guide finances publiques ; une incidence sur les retraites déclenche le guide retraites même si la fiche est classée emploi.
3. Préparer, pour chaque mesure, un relevé selon le [modèle de contrôle](../modeles/controle-domaines.md), dans `consolidation/controles-domaines/<mesure-id-ou-extraction-id>.json` de sa session locale.
4. Traiter chaque identifiant `COM-*` et chaque contrôle des guides chargés. Une ligne peut renvoyer aux preuves déjà utilisées par une autre ; ne pas refaire une recherche identique. Ne jamais cocher implicitement les contrôles non examinés.
5. Alimenter la recherche indépendante puis la fiche publique : données publiques pertinentes, comparaison prudente, guides et versions appliqués, lacunes et limites. Le relevé local ne remplace pas les sources publiques de la fiche.

Les contrôles s’appliquent à la proposition étudiée. Une mesure étroite ne justifie pas une analyse de toute la politique sectorielle. Un guide suggéré comme complément n’est chargé que si son mécanisme est concerné ; ne pas suivre récursivement tous les liens.

## Résultats permis pour chaque contrôle

| Résultat | Condition et information à fournir |
| --- | --- |
| `documente` | Réponse précise, sources consultées, repères et limites. Cela signifie « question documentée », jamais « promesse validée ». |
| `non_trouve` | Recherche effectivement menée mais sans réponse pertinente : producteurs, publications ou requêtes, dates, obstacles et limites. Un lien inaccessible seul appelle une recherche alternative raisonnable. |
| `non_applicable` | Motif lié à la mesure précise, sans éluder un effet explicitement annoncé. |
| `a_completer` | Contrôle non mené ou recherche interrompue. Empêche de déclarer la consolidation de cette mesure terminée. |

La consolidation peut avancer après une recherche infructueuse documentée, en conservant les lacunes dans la fiche. Elle ne peut pas transformer un `non_trouve` en coût nul, en réfutation ou en corroboration. Les autres mesures suffisamment documentées peuvent avancer si une fiche reste en attente.

## Domaines communs

Utiliser les identifiants ci-dessous pour `domaine_principal` et `domaines_secondaires` ; afficher les libellés français dans les index. Une mesure garde un seul fichier, même si plusieurs guides s’appliquent.

| Identifiant | Domaine et guide | Déclencheurs |
| --- | --- | --- |
| `finances-publiques-fiscalite` | [Finances publiques et fiscalité](domaines/finances-publiques-fiscalite.md) | Impôts, taxes, dette, déficit, économies budgétaires, dépenses nouvelles, niches fiscales ou financements |
| `emploi-salaires-pouvoir-achat` | [Emploi, salaires et pouvoir d’achat](domaines/emploi-salaires-pouvoir-achat.md) | SMIC, salaires, temps de travail, assurance chômage, formation professionnelle, prix, consommation ou emploi. |
| `retraites` | [Retraites](domaines/retraites.md) | Âge de départ, durée de cotisation, pensions, minimum de pension, financement, régimes spéciaux, pénibilité ou capitalisation. |
| `sante` | [Santé](domaines/sante.md) | Hôpital, soins, prévention, assurance maladie, médicaments, santé mentale, santé environnementale ou déserts médicaux. |
| `solidarites-famille-autonomie-handicap` | [Solidarités, famille, autonomie et handicap](domaines/solidarites-famille-autonomie-handicap.md) | Minima sociaux, pauvreté, allocations, petite enfance, aidants, dépendance, handicap, accessibilité ou protection de l’enfance. |
| `education-recherche` | [Éducation, enseignement supérieur et recherche](domaines/education-recherche.md) | École, université, apprentissage, orientation, étudiants, enseignants, recherche publique ou financement de l’innovation scientifique. |
| `logement` | [Logement](domaines/logement.md) | Construction, loyers, logement social, accession, hébergement, fiscalité immobilière, rénovation ou précarité énergétique. |
| `energie` | [Énergie](domaines/energie.md) | Électricité, nucléaire, renouvelables, gaz, pétrole, prix de l’énergie, sobriété, stockage ou indépendance énergétique. |
| `climat-biodiversite-eau` | [Climat, biodiversité, eau et ressources](domaines/climat-biodiversite-eau.md) | Émissions, adaptation, pollution, biodiversité, artificialisation, eau, déchets, recyclage, ressources naturelles ou risques environnementaux. |
| `transports` | [Transports et mobilités](domaines/transports.md) | Rail, route, transports collectifs, mobilité rurale, automobile, vélo, fret, aviation, infrastructures ou gratuité. |
| `agriculture-alimentation` | [Agriculture, pêche et alimentation](domaines/agriculture-alimentation.md) | Revenus agricoles, alimentation, élevage, pêche, pesticides, agriculture biologique, souveraineté alimentaire ou aides agricoles. |
| `industrie-commerce` | [Industrie, entreprises et commerce](domaines/industrie-commerce.md) | Réindustrialisation, relocalisation, PME, aides aux entreprises, nationalisation, commerce extérieur, concurrence ou politique industrielle. |
| `securite` | [Sécurité](domaines/securite.md) | Police, gendarmerie, délinquance, violences, ordre public, terrorisme ou prévention. |
| `justice` | [Justice](domaines/justice.md) | Procédures, tribunaux, peines, prisons, réinsertion, accès au droit ou justice des mineurs. |
| `immigration` | [Immigration, asile et intégration](domaines/immigration.md) | Entrées, séjour, asile, éloignement, nationalité, intégration, droits sociaux ou effets économiques de l’immigration. |
| `institutions-democratie` | [Institutions et démocratie](domaines/institutions-democratie.md) | Constitution, référendum, mode de scrutin, représentation, participation, décentralisation institutionnelle ou transparence publique. |
| `territoires-services-publics-outremer` | [Territoires, services publics et outre-mer](domaines/territoires-services-publics-outremer.md) | Décentralisation, ruralité, quartiers, accès aux services, fonction publique, organisation territoriale ou outre-mer. |
| `europe-international` | [Europe et relations internationales](domaines/europe-international.md) | Union européenne, traités, diplomatie, commerce international, aide au développement, sanctions ou coopération. |
| `defense` | [Défense](domaines/defense.md) | Armées, dissuasion, équipements, engagements militaires, réserves, alliances ou industrie de défense. |
| `numerique` | [Numérique, données et intelligence artificielle](domaines/numerique.md) | Couverture réseau, services numériques, IA, données personnelles, cybersécurité, plateformes ou souveraineté numérique. |
| `culture-sport` | [Culture, médias et sport](domaines/culture-sport.md) | Création, patrimoine, audiovisuel public, médias, pratiques culturelles ou sportives, équipements et grands événements. |
| `egalite-libertes-laicite` | [Égalité, libertés, discriminations et laïcité](domaines/egalite-libertes-laicite.md) | Égalité femmes-hommes, discriminations, libertés, laïcité, droits des personnes, accessibilité ou évolutions de droits civils. |

Si aucun domaine ne convient, utiliser provisoirement `autres`, appliquer le socle et consigner les questions propres au sujet. Proposer un complément de guide au coordinateur plutôt que classer de force ; signaler cette limite dans la fiche. Un agent candidat ne modifie pas seul les règles communes.

## Exemple de routage

Pour un changement d’âge de retraite : socle commun + retraites + emploi si les effets sur les seniors sont concernés + finances publiques si un coût ou financement est annoncé. Rechercher notamment les horizons démographiques cités, les recettes réellement observées, les dépenses des régimes, les contributions de l’État employeur et les éventuels transferts vers d’autres prestations. Reconstituer les flux sans doubler la contribution d’un ministère et la pension qu’elle finance.

## Entretien

Conserver les identifiants des contrôles ; ajouter de nouveaux identifiants sans réutiliser ceux supprimés. Dater toute modification de fond du guide et noter les points modifiés dans son historique. Un rafraîchissement réexamine les contrôles dont les sources, le mécanisme ou le guide ont changé ; ne pas recopier un ancien bilan sans vérifier sa pertinence. La version initiale de tous les guides est le 2026-10-15.
