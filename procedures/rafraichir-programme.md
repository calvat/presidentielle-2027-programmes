# Rafraîchir le programme d’un candidat

## Déclenchement

Appliquer cette procédure à une demande telle que « rafraîchis le programme de Mélenchon », « mets à jour les mesures de Jean-Luc Mélenchon » ou « collecte les nouveautés de ce candidat ». Elle fonctionne avec des outils de navigation et de fichiers ; aucun MCP propre au projet n’est requis. Ne pas prétendre qu’une simple instruction assure une exécution identique dans tous les clients.

Résoudre le nom via `candidats/README.md` et les index des candidats. En cas d’ambiguïté réelle, demander une précision avant de collecter. Lire les consignes du dépôt, la méthodologie et le README du candidat ; ce dernier contient les sites de départ.

## Démarrer dans un nouveau clone

Les points d’entrée des différents assistants sont décrits dans le [README](../README.md). Lire les fichiers de méthode depuis ce clone ; ne pas dépendre d’une mémoire personnelle ni d’un historique de conversation externe. Si le client n’a pas détecté les consignes, lire explicitement `AGENTS.md`, puis la présente procédure.

Vérifier les outils disponibles : lecture/écriture du dépôt, consultation des sources en ligne et Python 3.9+ avec le fuseau `Europe/Paris` pour le script de préparation. Respecter les permissions du client ; ne pas les modifier pour lancer la collecte. Aucun MCP propre au projet et aucune dépendance PyYAML ne sont nécessaires. Sans accès Web, ne pas prétendre avoir rafraîchi les sources.

Git ne conserve pas les dossiers vides. Si `candidats/<identifiant>/mesures/` ou `sources/references/` manque, considérer qu’aucune fiche n’y est encore disponible ; créer le dossier lors de la première écriture autorisée. Les agents candidats restent limités à leur candidat ; la création de références communes respecte la coordination décrite ci-dessous.

## Isolation obligatoire par candidat

Un agent chargé du contenu est affecté à **un seul candidat pendant toute sa durée de vie** : collecte, extraction, consolidation et mise à jour des fiches. Ne jamais réutiliser cet agent pour un autre candidat, même après la fin de son lot. Chaque nouvel agent reçoit explicitement l’identifiant unique du candidat, son README, sa session et ses chemins autorisés.

Pour trois candidats, lancer au minimum trois agents distincts, un par candidat. Les exécutions peuvent être successives si le client manque de places simultanées ; le nombre de places ne justifie pas de réaffecter un agent. Si le client ne permet pas plusieurs agents, utiliser des sessions séparées, chacune limitée à un candidat, et signaler cette contrainte ; ne pas annoncer une délégation inexistante.

Un coordinateur multi-candidats peut distribuer les missions et rassembler les bilans, mais ne collecte ni ne consolide lui-même le contenu de plusieurs candidats. Les éventuels sous-agents d’un candidat héritent exclusivement de ce même candidat ; ils ne lisent ni n’écrivent les dossiers ou espaces de travail des autres candidats. Les documents de méthode et références institutionnelles communes peuvent être consultés.

Un seul agent responsable écrit les fiches publiques et le README d’un candidat à la fois. Les sous-agents collecteurs écrivent dans des sous-dossiers distincts de sa session. Ne pas lancer deux rafraîchissements concurrents sur le même candidat. Pour une référence institutionnelle commune à créer ou corriger, préparer une proposition sourcée dans la session et transmettre au coordinateur pour intégration séquentielle ; éviter toute écriture concurrente dans `sources/` ou les index globaux.

Ces règles sont des consignes de travail, pas un cloisonnement de sécurité du système de fichiers. Documenter les affectations dans le manifeste et contrôler le périmètre des fichiers modifiés avant de conclure.

## Modèles et coût

Privilégier les modèles modestes pour découvrir les liens, collecter, extraire et classer les documents. Dans Codex, Luna convient ; dans un autre outil, utiliser son équivalent disponible. Ne pas imposer de fournisseur ou de modèle au corpus. Si le client ne permet pas de choisir le modèle, ne pas annoncer qu’un modèle différent a été utilisé.

Affecter par défaut un agent modeste par candidat, responsable du cycle complet. Si une collecte parallèle est utile, limiter initialement à deux collecteurs pour ce même candidat, sur des lots disjoints, puis confier la consolidation à son unique responsable. Ne pas faire lire le site entier par chaque agent. Le coordinateur réutilise leurs bilans plutôt que reprendre toute l’exploration.

### Travaux techniques délégables

Distinguer l’**agent de gestion** (modèle moyen, un seul candidat, jugement : choix des sources, lecture des extractions, décisions de consolidation, rédaction des fiches) des **exécutants techniques** (modèle le plus économique disponible, plusieurs en parallèle, éventuellement partagés entre candidats) qui reçoivent une consigne fermée et ne tranchent rien :

- téléchargement d’URL listées, empreintes, métadonnées d’accès (en-têtes, dates, statut) ;
- extraction du texte de PDF ou de pages en **texte verbatim** avec repères (URL, page, empreinte), jamais en résumé ;
- mise en forme et retraitement purement techniques (nettoyage, conversion, découpage par page ou rubrique) ;
- récupération de séries ou tableaux institutionnels selon des paramètres fixés par le gestionnaire.

Règles : préférer un script déterministe à un exécutant (`scripts/verifier_sources.py` en est un) ; chaque exécutant écrit dans un sous-dossier disjoint de la session et ne lit que les chemins de sa consigne ; il ne sélectionne, n’interprète ni ne résume. L’isolation par candidat vise le contenu : un exécutant technique sans contenu à interpréter peut traiter des lots de plusieurs candidats, à condition de ne mélanger ni leurs dossiers ni leurs sessions. Le gestionnaire ne cite que depuis le texte verbatim conservé, et contrôle que chaque extrait cité y figure ; un résumé produit par un outil ou un agent ne constitue pas une source. Le gestionnaire reste responsable du résultat.

Réserver une éventuelle escalade de modèle aux difficultés précises et non résolues. Ne pas lancer automatiquement un modèle plus coûteux pour l’ensemble du site. Identifier d’abord ce qui manque et réduire le lot ou laisser le point explicitement incertain.

## 1. Préparer une session locale

Depuis la racine :

```sh
python3 scripts/preparer_collecte.py jean-luc-melenchon
```

Le script crée `candidats/<identifiant>/_travail/collectes/<session>/`, son `manifest.json` et ses dossiers `brut/`, `extractions/` et `consolidation/`. Ce répertoire de travail propre au candidat est ignoré par Git. Les sessions précédentes sont conservées, jamais écrasées.

Si Python ou les données de fuseau nécessaires ne sont pas disponibles, signaler la limite et préparer manuellement la même structure avec les outils de fichiers du client : lire `scripts/preparer_collecte.py` comme définition du manifeste, reproduire ses champs initiaux, choisir un identifiant de session unique et enregistrer une date réelle avec sa précision et son fuseau connus, sans inventer d’heure. Vérifier que le candidat existe, que les répertoires de travail ne sont pas des liens symboliques et qu’aucune session n’est écrasée. Cette solution ne dispense d’aucune étape de collecte, de contrôle ni de consolidation. Ne pas installer de dépendance ou changer les permissions du client implicitement.

Renseigner dans le manifeste `agent_responsable`, `agents` (identifiant, candidat unique, rôle et sous-dossier) et `fichiers_modifies`. Enregistrer l’état initial des fichiers du candidat pour distinguer les changements de cette session des changements préexistants.

Lire la dernière session locale et les fiches existantes avant de naviguer. Dans un nouveau clone, les bruts sont absents : reconstruire la collecte depuis les sources publiques et les références des fiches ; ne pas prendre cette absence locale pour un retrait de mesure.

## 1 bis. Détecter ce qui a changé

Avant de naviguer, lancer depuis la racine :

```sh
python3 scripts/verifier_sources.py jean-luc-melenchon
```

Le script lit `candidats/<identifiant>/suivi-sources.json`, récupère chaque URL, normalise le texte visible, compare son empreinte à celle du registre et classe chaque source : `inchangee`, `modifiee`, `nouvelle` (absente du registre), `inaccessible`. Il n’écrit dans le registre qu’avec `--ecrire`, après examen. Utiliser le résultat ainsi :

- `inchangee` : ne pas relire ni réextraire ; mettre à jour `dernier_controle_presence` des mesures qui s’appuient sur cette source et consigner « source inchangée à la date du contrôle » dans leur historique.
- `modifiee` : réextraire seulement cette source, comparer à l’extraction précédente et ne retravailler (recherche indépendante comprise) que les mesures dont le contenu change.
- `nouvelle` ou `inaccessible` : traiter comme dans la section 2 ; une page inaccessible ne prouve aucun retrait.

Limites à rappeler dans le bilan : l’empreinte du texte visible peut changer sans modification de fond (bandeaux, dates, listes d’articles) et ne change pas lorsque le contenu est servi dynamiquement ou dans un PDF non relu ; l’absence de changement détectée n’est pas une preuve d’identité. Les index de rubriques restent contrôlés pour repérer de nouveaux documents. Sans accès réseau, signaler que la détection n’a pas pu être faite.

## 2. Collecter avant de consolider

Partir du tableau des URL de collecte ciblée du README et des sites officiels. Consulter en priorité les index et documents déjà connus ; parcourir de nouveau l’ensemble du site seulement si nécessaire. Lors de chaque session, vérifier aussi les index de rubriques pour découvrir de nouveaux documents ; ne pas limiter la collecte aux seules URL mémorisées. Actualiser le tableau avec les nouveaux liens, leur utilité et le résultat du contrôle. Inventorier programme actuel, documents du parti pertinent, plans, discours et interviews accessibles. Consulter les sources originales. Distinguer pages découvertes et pages effectivement lues ; séparer documents actuels, éditions anciennes et dates inconnues.

Constituer un premier lot utile et limité, puis élargir selon le besoin. Ne pas revendiquer un rafraîchissement complet sur la base de ce lot ; inscrire les rubriques restantes dans le manifeste. Pour une mise à jour, prioriser les nouveaux documents et les sources des mesures existantes. Si disponibles, comparer empreintes, dates ou versions ; leur absence ne prouve pas qu’une page n’a pas changé.

Dans `manifest.json`, ajouter une entrée par source dans `sources` avec :

- `id`, `url`, `url_finale`, `titre`, `type_document`, `auteur` ;
- `consulte_le` (horodatage avec fuseau si enregistré, sinon date avec `precision_consultation: jour` ; ne pas inventer une heure), `date_publication`, `date_intervention`, `lieu` lorsque connus, sinon `null` ;
- `statut_acces` : `consulte`, `decouvert_non_consulte`, `inaccessible` ;
- `edition`, `licence`, `url_droits`, `mode_conservation` (`lien_seul`, `extrait`, `copie_autorisee`) ;
- `fichier_local` s’il existe, `empreinte_sha256` si calculée, et `limites`.

Enregistrer dans `brut/` les éléments réellement observés et leur provenance : texte ou fichier lorsque la conservation est autorisée, sinon lien, métadonnées et courts extraits lorsque leur usage le permet. L’ignorance par Git n’accorde aucun droit supplémentaire, ne constitue pas une protection de confidentialité et n’exclut pas la lecture par l’assistant. Ne pas envoyer les bruts vers un dépôt ou un service externe par défaut.

Conserver les bruts sans réécriture éditoriale. Mettre les propositions de découpage et interprétations dans `extractions/`, avec source et repère pour chaque élément. Ne pas produire de fiches publiques pendant la collecte. Les obstacles d’accès et les dates inconnues sont enregistrés ; ne pas les combler par supposition.

## 3. Terminer le lot de collecte

Attendre les résultats des collecteurs actifs avant la consolidation du lot. Rassembler le manifeste, dédupliquer les URL et conserver les variantes de documents significatives. Renseigner `perimetre`, `lacunes`, `etat_collecte` (`partielle` ou `terminee_sur_perimetre`) et la liste des fichiers de collecte. « Terminée sur périmètre » ne veut pas dire exhaustive du programme.

Une demande limitée à la collecte s’arrête ici. Indiquer les chemins locaux et ce qui reste à explorer. Les dates de collecte et l’état des sources sont factuels, sans qualification de validité du programme.

## 4. Rechercher les données publiques et éléments indépendants

Cette étape est obligatoire pour chaque mesure à créer ou modifier, avant sa consolidation finale et son écriture dans le dépôt. Le corpus politique seul ne suffit pas à terminer un rafraîchissement.

### 4.1. Définir les vérifications adaptées au sujet

Lire `guides/README.md`, le socle commun et les guides correspondant au domaine principal ainsi qu’aux effets secondaires réellement concernés. Ne pas charger tous les guides. Toute annonce de coût ou financement public déclenche aussi le guide finances publiques. Les questions de démographie, de budgets connexes et de transferts ne doivent pas être oubliées au seul motif que le candidat ne les mentionne pas.

Créer un relevé par mesure selon `modeles/controle-domaines.md` dans `consolidation/controles-domaines/`, avec candidat unique, identifiant de mesure ou d’extraction, guides, versions et date. Recenser les identifiants attendus du socle et des guides chargés. Traduire chacun en question concrète pour la proposition ; justifier les cas non applicables. Ce relevé guide les recherches ci-dessous.

### 4.1 bis. Réutiliser avant de rechercher

Les faits externes sont mutualisés : `sources/references/` contient une référence par série ou publication, utilisée par tous les candidats. Avant toute recherche :

1. Lire `sources/references/INDEX.md` (références par domaine, statut, date de consultation, date de revalidation, fiches qui les citent) et `sources/lacunes.md` (recherches infructueuses et accès bloqués déjà documentés).
2. Réutiliser une référence existante si son indicateur, son périmètre et son millésime conviennent. Ne pas refaire une recherche déjà consignée dans `lacunes.md` sauf si sa date de réessai est atteinte ou si l’utilisateur demande un rafraîchissement profond.
3. Ne **pas** revérifier une référence dont la donnée est définitive, ni dont `revalider_apres` est postérieure à la date du jour. Revérifier une référence provisoire seulement lorsque sa date de revalidation est échue ou qu’une révision est connue. Consigner dans le bilan « référence réutilisée sans recontrôle » avec sa date de dernière consultation.
4. Ne créer une nouvelle référence que pour une donnée absente ; la rédiger selon `modeles/reference.md`, avec ses champs de revalidation, puis régénérer l’index avec `python3 scripts/indexer_references.py`. Ne jamais recopier une valeur de référence dans une fiche : renvoyer à la référence (identifiant, version, indicateur). Ajouter à `lacunes.md` toute recherche qui n’a rien donné ou dont l’accès est bloqué.
5. Un **rafraîchissement profond** (demande explicite : « rafraîchissement profond », « revérifie toutes les données ») recontrôle chaque référence concernée dans sa publication d’origine, met à jour version et date de consultation, et signale les révisions et leur effet sur les fiches qui les citent.

### 4.2. Chercher, comparer et enregistrer les preuves

1. Identifier les affirmations chiffrées du candidat, les grandeurs utiles au sujet et les questions auxquelles des données publiques peuvent répondre : situation actuelle, population concernée, dépenses existantes, tendances, comparaisons pertinentes. Distinguer ce contexte d’une évaluation du coût ou des effets futurs de la mesure.
2. Chercher d’abord dans `sources/references/`. Contrôler que les références existantes sont pertinentes, suffisamment récentes et comparables. Lire ensuite `sources/organismes.md`, les points d’entrée pertinents de `sources/reperes-domaines.md` et rechercher les publications d’origine des producteurs pertinents qui y sont répertoriés. Ce répertoire constitue un point de départ de confiance, pas une validation automatique des chiffres ; il ne contient pas encore nécessairement les données recherchées.
3. Si nécessaire, collecter les séries ou publications manquantes auprès de ces organismes nationaux et internationaux, selon `sources/README.md`. Une nouvelle source non répertoriée peut être proposée avec justification de sa compétence, de sa méthode et de son indépendance. Ne pas utiliser une reprise médiatique ou un chiffre de campagne comme substitut à une publication d’origine disponible.
4. Rechercher également les évaluations indépendantes directement pertinentes lorsqu’elles existent, sans confondre une statistique descriptive avec une estimation du coût de la mesure. Documenter auteur, méthode, hypothèses, éventuels liens politiques et incertitudes. Une estimation extérieure ne devient pas une vérité par sa seule indépendance.
5. Mettre en regard les grandeurs uniquement si période, territoire, population, unité, définition et périmètre le permettent. Présenter les différences restantes. Ne pas fabriquer un « contre-chiffrage », une causalité ou une conclusion de faisabilité à partir de simples ratios. Toute opération de l’agent est un calcul explicitement identifié.

Consigner dans `consolidation/recherche-independante.json` une entrée par mesure ou élément candidat : `candidat`, `mesure_id` ou identifiant d’extraction, `questions`, `affirmations_candidat`, `references_repo_consultees`, `recherches_effectuees` (organisme, URL ou requête et date), `references_retenues`, `comparabilite`, `limites`, `controles_domaines` (chemin du relevé local, guides et versions) et `resultat` (`donnees_trouvees`, `donnees_partielles`, `aucune_donnee_pertinente_trouvee` ou `recherche_incomplete`). Lier ce bilan aux décisions de consolidation. Une recherche infructueuse ne doit pas être remplacée par un champ « à renseigner » sans tentative documentée.

Préparer les nouvelles références selon `modeles/reference.md` dans la session locale. Les faire intégrer séquentiellement à `sources/references/` par le coordinateur, ou par le responsable du candidat si son mandat lui réserve explicitement cette écriture commune. Avant de publier une fiche, vérifier que ses liens vers les références du dépôt existent réellement. La fiche renvoie à ces références (identifiant, version, indicateur) au lieu de recopier leurs valeurs ; l’URL d’origine et la version restent dans la référence, qui est publique : les éléments probants ne dépendent pas du dossier ignoré.

Renseigner chaque contrôle du relevé avec `documente`, `non_trouve`, `non_applicable` justifié ou `a_completer`, en liant les preuves et recherches. Vérifier la présence de tous les identifiants attendus, sans doublon. Un contrôle documenté peut constater une incertitude ou une absence de paramètre ; il ne valide pas le chiffrage du candidat.

La condition de passage est une recherche effectivement menée et documentée, avec tous les contrôles applicables traités et aucun `a_completer`, pas l’obtention forcée d’un chiffre. Si aucune donnée pertinente n’est disponible malgré la recherche, la fiche peut être consolidée en l’indiquant explicitement, avec les limites et sans conclusion sur la validité du chiffrage candidat. Une recherche non effectuée ou inachevée laisse la consolidation de cette mesure en attente et le rafraîchissement partiel ; les autres mesures suffisamment documentées peuvent avancer.

## 5. Consolider les mesures

**Une demande de rafraîchissement implique par défaut la consolidation ET l’écriture effective des fiches et de l’index du candidat dans le dépôt.** Ne pas s’arrêter à une collecte, un plan ou des propositions de modifications. Seule une demande explicitement limitée à la collecte s’arrête à l’étape 3. Continuer sans validation humaine de routine.

Établir dans `consolidation/` une correspondance entre éléments bruts et fiches : création, précision, doublon, remplacement, retrait explicite ou incertitude. Chaque décision cite les identifiants de sources et repères consultables. Ne pas transformer les documents 2022/2025 en engagements de 2027 sur la seule présence d’un lien actuel.

Le plan local `consolidation/decisions.json` contient une entrée par élément examiné : `candidat`, `sources`, `reperes`, `mesure_id` si identifiée, `action`, `justification`, `chemin_cible`, `bilan_recherche_independante`, `controles_domaines` et `etat_application`. Les actions possibles sont `creer`, `modifier`, `confirmer_sans_changement`, `remplacer`, `retrait_explicite`, `doublon` ou `laisser_incertain`. Un élément insuffisamment sourcé ne devient pas une fiche présentée comme établie.

Comparer chaque proposition aux fiches existantes avant de créer un identifiant. Une même mesure retrouvée dans une interview et un programme doit enrichir la fiche existante, sans créer un doublon. Ne pas attribuer un nouvel identifiant à une simple reformulation ou précision.

Rédiger ou actualiser une fiche par mesure selon `modeles/mesure.md`, avec identifiant stable, dates d’observation réelles et statut. Distinguer propos du candidat, propositions du parti, chiffres annoncés, références institutionnelles et calculs. La fiche comprend obligatoirement une section « Données publiques sur le sujet », une section distincte d’analyses indépendantes et une mise en regard avec les chiffres du candidat, alimentées par l’étape 4. Renseigner aussi les guides et versions appliqués ainsi que le bilan des contrôles par domaine prévu dans le modèle. Les recherches infructueuses et limites restent visibles ; une vérification non menée garde la consolidation en attente. Ne pas présenter le contexte public comme une validation des effets annoncés.

Ne retirer une mesure des engagements actuels que sur un fondement documenté ; une page absente ou inaccessible ne prouve pas l’abandon. Conserver l’historique. Appliquer les droits par source : les bruts ne sont pas copiés automatiquement dans les fichiers publics, et les citations ou adaptations ne deviennent pas CC0.

Mettre à jour le README du candidat avec toutes les mesures, leurs domaines, descriptions, statuts et dates. Vérifier les liens relatifs et l’absence de fiches orphelines. Aucun index public ne doit dépendre d’un fichier ignoré pour permettre de vérifier une affirmation : conserver les références originales et repères publics.

## 6. Appliquer les décisions au dépôt

Le responsable du candidat applique effectivement les décisions étayées dans `candidats/<identifiant>/mesures/`, puis actualise `candidats/<identifiant>/README.md` avec liens, mini-descriptions, domaines, statuts, dates, URL de collecte et limites de couverture. Il ne modifie aucun dossier d’un autre candidat.

Pour chaque décision, renseigner `etat_application` (`appliquee`, `sans_modification_necessaire` ou `non_appliquee`) et le motif si elle ne peut pas être appliquée. Lister les chemins réellement modifiés dans le manifeste. Préserver les modifications préexistantes, les identifiants stables et l’historique des mesures.

Une confirmation de présence peut mettre à jour la dernière observation ; une consultation infructueuse ne le peut pas. En l’absence de nouvelles mesures, de nouvelles informations ou de changement documenté, ne pas inventer de modifications de fond : consigner le contrôle et son résultat.

En cas d’accès ou de preuve insuffisants, appliquer les seules décisions étayées et déclarer la consolidation partielle avec ses raisons. Ne pas marquer la session comme terminée sur son périmètre tant que des décisions applicables restent simplement en attente d’écriture.

## 7. Contrôler et rendre compte

Vérifier que `_travail/` est ignoré avec `git check-ignore`, qu’aucun brut n’a été ajouté au suivi Git, que les JSON sont lisibles, les sources attribuées et les liens internes valides. Ne pas utiliser `git add -f` pour contourner l’exclusion. Ne pas annoncer une relecture humaine.

Contrôler que tous les fichiers modifiés par l’agent appartiennent au candidat affecté ou à une intégration commune explicitement coordonnée. Vérifier l’absence de doublons et la correspondance entre le journal de décisions, les fiches et l’index. Vérifier pour chaque fiche la recherche indépendante documentée, la présence des données publiques ou du constat motivé de leur indisponibilité, et la validité des liens vers les références communes. Contrôler la couverture des identifiants du socle et des guides appliqués, les preuves des résultats et l’absence de `a_completer` pour les mesures déclarées consolidées. Vérifier que les lacunes importantes apparaissent dans les fiches publiques et pas seulement dans les relevés ignorés.

Renseigner `etat_recherche_independante` (`non_commencee`, `partielle`, `terminee_sur_perimetre`) et `bilans_recherche_independante` dans le manifeste. Une recherche terminée peut constater des données indisponibles ; elle ne signifie pas que toutes les affirmations sont vérifiées.

Mettre à jour le manifeste avec `etat_consolidation` (`non_commencee`, `partielle`, `terminee_sur_perimetre`). En cas d’interruption, le manifeste et les fichiers existants permettent de reprendre sans repartir de zéro. Ne pas effacer les sessions antérieures.

Le rafraîchissement est terminé sur son périmètre seulement si la collecte du lot est terminée, la recherche indépendante est effectuée pour toutes les mesures traitées, les contrôles par domaine sont documentés sans point à compléter pour les mesures consolidées, les décisions étayées sont appliquées, l’index est cohérent et les contrôles réussis. Une collecte exploratoire non exhaustive reste décrite comme telle, même après application de toutes les décisions du lot.

Rapporter : candidat unique, agent responsable, périmètre parcouru, sources consultées, fiches créées ou modifiées, retraits établis, incertitudes, emplacement local des bruts et limites de couverture. Aucun commit, push ou publication externe n’est requis par cette procédure seule.
