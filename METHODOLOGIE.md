# Méthodologie

## Périmètre

Documenter les propositions publiques relatives à la présidentielle française de 2027. Toute fiche précise l’auteur de la proposition, la date et la nature du document. Une position ancienne ou un programme de parti peut apporter du contexte, mais ne devient pas automatiquement une proposition personnelle pour 2027.

Le corpus est progressif. Sa couverture doit être rendue visible ; la quantité de documents disponibles ne constitue pas une mesure de la qualité d’un programme.

## Candidats suivis

Commencer avec une liste volontairement restreinte de candidatures confirmées par une annonce explicite et une source primaire datée. Exclure les personnes seulement pressenties, les rumeurs et les simples intentions conditionnelles. Avant la publication de la liste officielle, utiliser « candidature annoncée et confirmée », sans prétendre à une validation officielle. Une fois cette liste publiée, ne conserver que les candidats officiellement retenus.

### Sélection initiale et élargissement

Dans la phase préparatoire, donner priorité aux candidatures ayant atteint **environ 5 % ou davantage au moins une fois** dans un sondage national d’intentions de vote au premier tour de la présidentielle de 2027. Ce repère permet de concentrer les moyens de collecte sur un nombre limité de dossiers pendant que de nombreuses candidatures restent susceptibles d’évoluer. Il ne mesure ni la qualité d’un programme, ni la légitimité d’une candidature, ni sa certitude de figurer au scrutin. Ne pas publier une proportion anticipée de retraits sans source.

Ce repère est indicatif : pour un résultat proche de 5 %, conserver le score exact et expliquer le choix, sans arrondir silencieusement ni fixer une tolérance arbitraire. Ne pas remplacer ce critère documentable par une appréciation subjective de notoriété ou de « sérieux ».

Pour chaque inclusion, consigner dans le README du candidat le motif de sélection et la référence du sondage : institut, commanditaire, dates de terrain et de publication, population interrogée, score exact, scénario de candidatures testé et lien vers le tableau ou rapport d’origine consulté. Un article peut aider à trouver le sondage ; privilégier ses résultats originaux. Ne pas assimiler consultation ouverte sur Internet, cote de popularité, intention de vote à une primaire ou au second tour à ce critère de premier tour. Les scores publiés restent des estimations avec leur méthode et leurs incertitudes.

Une présence dans un scénario de sondage ne constitue pas une annonce de candidature. Les conditions de candidature et le motif de sélection sont documentés séparément. Une baisse ultérieure du score ne déclenche pas automatiquement une suppression puisque le repère porte sur au moins une observation. L’ajout de cette règle ne vaut pas vérification rétrospective des sondages des dossiers déjà ouverts : indiquer « critère d’audience à documenter » tant que sa référence manque.

Élargir progressivement la liste lorsque les candidatures se précisent, que de nouveaux éléments le justifient ou que la liste officielle est publiée. Le repère initial n’est pas une exclusion définitive des autres candidats. Afficher les limites de couverture et ne pas présenter les personnes suivies comme l’ensemble des candidats à l’élection.

En cas de retrait, de renoncement ou de non-validation, supprimer le dossier du candidat du corpus courant et retirer ses entrées des index et comparaisons, avec une source datée justifiant ce changement. L’historique Git reste conservé ; ne pas réécrire cet historique. Ne pas supprimer une mesure isolée uniquement parce que le candidat en a changé : documenter son évolution tant que le candidat reste suivi.

## Sites officiels de départ

Chaque candidat possède dans son `README.md` un répertoire des sites officiels et des rubriques de collecte, avec rôle, justification et date de consultation. Les agents le consultent avant toute collecte et commencent par ces sources primaires, sans limiter les vérifications aux sources de campagne. Les références finales pointent vers les documents précis. Documenter les droits de réutilisation et distinguer les éditions anciennes des engagements actuels.

## Sources admises et attribution

- **Interviews et entretiens** : inclure les propositions exprimées, avec un court extrait exact, le lien vers le document original (texte, audio ou vidéo), le nom du média et de l’intervieweur si disponible, la date de l’entretien et celle de publication si différente, ainsi que la page ou le minutage de début et de fin. Conserver la question ou le contexte nécessaire à la compréhension de la réponse.
- **Propositions du parti du candidat** : les inclure lorsque le parti est bien celui du candidat, en documentant cette affiliation à la date pertinente. Identifier le parti comme auteur et préciser la date et la version du document. L’appartenance au même parti ne prouve pas que le candidat reprend personnellement chaque proposition : indiquer « proposition du parti — reprise personnelle non documentée » tant qu’une source ne démontre pas cette reprise.
- **Discours et interventions publiques** : relever les passages significatifs pour une proposition, une précision, un chiffrage ou une évolution de position. Fournir un court extrait exact, le lien vers le texte ou l’enregistrement, la date de l’intervention, le lieu (ville et salle si connus), l’événement et la page ou le minutage de début et de fin. Distinguer la date du discours de sa date de mise en ligne.

La sélection des passages repose sur leur contenu programmatique, avec les mêmes critères pour tous, sans privilégier les seules formules spectaculaires. Conserver les réserves et conditions qui modifient le sens de la déclaration. Un extrait ne doit pas être présenté comme la totalité d’une position.

Indiquer « non précisé dans la source » pour un lieu ou une date introuvable ; ne jamais les déduire sans preuve. Pour une intervention à distance, le signaler. Une transcription automatique doit être identifiée et contrôlée sur l’enregistrement avant d’être présentée comme une citation vérifiée ; sinon la marquer « transcription non vérifiée ».

Les positions antérieures à la campagne restent datées et identifiées comme contexte historique, sauf reprise explicite pour 2027. Si l’affiliation du candidat change, conserver l’attribution historique sans rattacher automatiquement les propositions de son ancien parti à son programme actuel.

## Règle de preuve

1. Retrouver et consulter la source de la proposition ; conserver une courte citation fidèle et un repère précis.
2. Rédiger un résumé descriptif sans ajouter d’intention ou d’effet non documenté.
3. Relever séparément les chiffres annoncés et leurs hypothèses. Leur statut initial est « déclaration du candidat — non vérifiée ».
4. Rechercher les données de référence et les analyses indépendantes pertinentes. Documenter leur auteur, leur méthode, leur date et leurs limites, y compris un éventuel lien avec une organisation politique.
5. Consigner les éléments corroborés, contestés et non vérifiables. Une vérification porte sur une affirmation précise, pas sur l’ensemble de la fiche.
6. Dater la fiche et renseigner son état de contrôle par IA avec exactitude.

## Base de données institutionnelles

Constituer progressivement une base de référence distincte des sources politiques, à partir de producteurs nationaux et internationaux compétents, notamment l’INSEE. Le protocole de collecte est décrit dans `sources/README.md` ; les organismes de départ figurent dans `sources/organismes.md`.

Chaque série ou publication possède une fiche selon `modeles/reference.md`. Les mesures citent cette référence commune et sa version. La collecte effective, les contrôles et les révisions doivent être documentés ; la seule présence d’un organisme dans le répertoire ne vaut ni collecte ni vérification.

## Sens du statut « vérifié »

Distinguer le contrôle documentaire par IA d’une fiche, le contrôle d’une citation et la vérification du fond d’une affirmation. Une fiche contrôlée ne certifie pas les déclarations qu’elle contient.

- **Donnée de référence vérifiée** : donnée contrôlée dans sa publication d’origine auprès d’un organisme statistique ou scientifique compétent, ou fait appuyé par un consensus scientifique ou technique documenté, indépendant des prises de position partisanes. Citer la publication et son périmètre ; ne pas inventer un consensus et ne pas compter plusieurs reprises d’une même source comme des confirmations indépendantes.
- **Déclaration ou estimation du candidat — non vérifiée** : prévision, coût, économie ou effet annoncé par le candidat ou son parti sans corroboration suffisante. Sa publication officielle ne suffit pas à la vérifier.
- **Estimation indépendante** : résultat d’une analyse extérieure, avec ses hypothèses et incertitudes. L’indépendance seule ne transforme pas une estimation en fait acquis.
- **Affirmation contestée ou données insuffisantes** : décrire précisément le désaccord ou le manque de preuve, sans arbitrage politique ni conclusion fabriquée.

Un PIB publié par l’organisme statistique compétent peut être utilisé comme donnée de référence vérifiée, avec année, territoire, unité, valeur ou volume, base et version de publication. Cela ne le rend pas immuable : signaler un statut provisoire, une révision ou une incertitude indiquée par le producteur. Distinguer un PIB observé publié d’une prévision de PIB et d’une interprétation politique de ce chiffre.

Un chiffre de référence repris par un candidat peut être corroboré en consultant sa source d’origine ; les effets futurs qu’il en déduit doivent être examinés séparément. Le consensus pertinent est scientifique, statistique ou technique, pas un accord entre responsables politiques.

## Chiffrages et comparaisons

Distinguer coût et financement, montants annuels et cumulés, brut et net, euros courants et constants, objectif et résultat observé. Ne pas comparer des nombres incompatibles sans expliquer les différences. Ne pas additionner des mesures dont les périmètres peuvent se recouper sans examiner les doubles comptes.

Une estimation indépendante reste une estimation. Présenter les hypothèses et les désaccords documentés plutôt que choisir arbitrairement un chiffre unique. Une donnée publique peut éclairer une proposition sans suffire à en démontrer les effets.

## Suivi temporel et abandon des mesures

Chaque mesure comporte `premiere_observation` et `derniere_observation`, correspondant aux dates auxquelles le projet a effectivement constaté sa présence dans une source consultée. Elles ne constituent pas une preuve de première annonce ni de dernière expression publique du candidat. Conserver séparément la date de publication ou d’intervention de chaque source, et `date_annonce` lorsqu’elle est établie.

`dernier_controle_presence` indique la date du dernier contrôle, y compris infructueux. Ne mettre à jour `derniere_observation` que si la mesure est effectivement retrouvée ou réaffirmée ; un échec d’accès ne suffit pas. Ne pas antidater les observations du projet à la date d’un document ancien.

Statuts communs :

- **documentée** : présence constatée dans les sources, sans retrait établi ; ce statut ne garantit pas un engagement actuel au-delà des sources consultées.
- **retrait explicite** : abandon établi par une déclaration ou un document explicite, cité et daté.
- **remplacée** : une source établit qu’une nouvelle proposition remplace la précédente ; relier les fiches.
- **non retrouvée lors du dernier contrôle** : absence constatée dans les sources contrôlées, sans preuve suffisante d’abandon.
- **statut incertain** : sources contradictoires, inaccessibles ou insuffisantes pour conclure.

Une absence dans un nouveau document, une page supprimée ou une erreur d’accès ne prouve pas à elle seule l’abandon. Consigner le périmètre du contrôle et les limites. En cas de changement, distinguer la date de constat du projet de la date effective annoncée par le candidat ; ne pas inventer cette dernière.

Conserver les fiches des mesures retirées ou remplacées et leur historique tant que le candidat reste suivi. Dans l’index, afficher leur statut et leurs dates ; ne pas les présenter comme des engagements actuels. Une évolution substantielle de proposition peut justifier une nouvelle fiche liée à l’ancienne ; une simple précision conserve l’identifiant avec une entrée dans l’historique.

## Corrections et suivi

Conserver les identifiants des mesures. Lors d’une modification ou d’un retrait, mettre à jour le statut et inscrire la date, la source et la nature du changement dans l’historique de la fiche. Git conserve les versions précédentes.

## Production et contrôles par IA

La collecte, la rédaction, les contrôles et les mises à jour sont effectués par IA. Aucune relecture humaine n’est prévue ni requise pour publier une fiche. Cette absence doit être indiquée dans la présentation du corpus et ne doit jamais être masquée par un label de validation humaine.

États du contrôle documentaire : « non effectué », « effectué par IA » ou « incomplet ». Consigner la date, les points contrôlés et les limites. Contrôler la consultation effective des sources, la fidélité des extraits, l’attribution, les dates, les unités et les liens vers les références. Un lien valide ne suffit pas : la source doit soutenir précisément l’affirmation associée. Un contrôle documentaire par IA n’est pas une certification de vérité.

## Index par candidat

Chaque dossier contient un `README.md` selon `modeles/candidat.md`, puis un dossier `mesures/`. L’index comporte une ligne par fiche avec identifiant stable, domaine principal, mini-description factuelle et lien relatif. Il est actualisé avec les fiches ; aucune mesure ne doit rester sans lien depuis cet index.

Utiliser les identifiants de domaine communs de [l’index des guides](guides/README.md), avec un domaine principal et les domaines secondaires pertinents. Afficher les libellés français dans l’index candidat. Le découpage distingue notamment retraites, santé, énergie, climat, sécurité et justice pour guider leurs vérifications propres. Une mesure reste dans un fichier unique. Pour un sujet non couvert, utiliser provisoirement `autres`, appliquer le socle et documenter les questions manquantes avant de proposer une extension commune.

## Droits par source

Appliquer CC0 uniquement aux contributions originales sur lesquelles les contributeurs disposent des droits nécessaires. Les documents de tiers sont conservés séparément avec une notice selon `modeles/document-source.md`, lorsque leur redistribution est autorisée ; à défaut, référencer l’original par un lien. Délimiter les extraits et indiquer leurs droits dans chaque fiche. Une adaptation doit être examinée au regard de sa source, même si elle est produite par IA. Les exports conservent ces distinctions et ne sont pas annoncés intégralement sous CC0. Voir `LICENSE.md`.

## Contexte public et confrontation indépendante

La consolidation finale de chaque mesure est précédée d’une recherche documentée de données publiques et d’analyses indépendantes, selon l’étape 4 de `procedures/rafraichir-programme.md`. Réutiliser les références communes contrôlées, puis compléter la base à partir des producteurs pertinents. Les fiches distinguent le contexte public, les estimations indépendantes et la mise en regard avec la déclaration du candidat.

L’obligation porte sur la recherche effective et sa traçabilité, sans imposer un chiffre artificiel lorsqu’aucune donnée pertinente n’existe. Une recherche infructueuse est un résultat documenté ; une recherche non menée ou inachevée laisse la consolidation en attente. Les statistiques descriptives ne suffisent pas à prouver la faisabilité, le coût ou les effets futurs d’une proposition.

## Vérifications par domaine

Les [guides](guides/README.md) reposent sur un [repérage documenté des thèmes de 2017 et 2022](guides/reperage-2017-2022.md), complété par un découpage méthodologique. Ce repérage n’est ni un dépouillement exhaustif des programmes ni une hiérarchie des enjeux.

Avant consolidation, appliquer le socle commun et les seuls guides pertinents. Chaque contrôle reçoit une réponse sourcée, une recherche infructueuse documentée, un motif de non-applicabilité ou un état à compléter. Ce dernier empêche de déclarer la mesure consolidée. Les chiffres de contexte, estimations indépendantes et effets allégués restent distincts, même lorsqu’un contrôle est documenté. Le relevé local suit `modeles/controle-domaines.md` ; les versions, références et lacunes utiles sont conservées dans la fiche publique.
