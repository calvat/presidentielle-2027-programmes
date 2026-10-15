# Présidentielle 2027 — Programmes

Un corpus documentaire en français pour explorer les programmes de la présidentielle de 2027 avec Codex, Claude Code, Cursor ou un autre assistant IA. Les informations sont conservées en Markdown, avec leurs sources, leurs dates et leurs limites.

Le projet documente les mesures, leurs sources, les chiffrages annoncés et les analyses indépendantes disponibles. Il ne recommande aucun candidat et ne produit aucun classement politique.

**Un chiffre publié par un candidat est une déclaration attribuée, pas un fait établi.** Une information absente du corpus ne permet pas de conclure à l’absence de proposition.

## État du projet

**Le dépôt est en construction.** Il contient huit dossiers de candidats, une méthode de collecte et 22 guides de vérification par domaine. Une première exploration a été menée pour Jean-Luc Mélenchon ; aucune fiche de mesure n’est encore consolidée et aucune exhaustivité n’est revendiquée. Les sondages justifiant le critère initial d’audience restent à documenter.

- [Parcourir les candidats](candidats/README.md)
- [Comprendre la méthode](METHODOLOGIE.md)
- [Consulter les guides de vérification](guides/README.md)
- [Lire la procédure de rafraîchissement](procedures/rafraichir-programme.md)
- [Consulter les sources de référence](sources/README.md)

## Démarrer

```sh
git clone https://github.com/calvat/presidentielle-2027-programmes.git
cd presidentielle-2027-programmes
```

Ouvrir ce dossier dans Codex, Claude Code ou Cursor en mode Agent, puis demander :

> Rafraîchis le programme de Mélenchon.

L’assistant suit les consignes du dépôt : collecte des sources dans un espace local ignoré par Git, recherche de données publiques et d’analyses indépendantes, puis consolidation et mise à jour des fiches et de l’index du candidat. Les prérequis et les points d’entrée de chaque assistant sont décrits [plus bas](#rafraîchir-un-programme-avec-un-assistant). Aucun MCP propre au projet n’est requis.

## Ce que contient une fiche de mesure

Une fiche distingue la proposition attribuée au candidat, son chiffrage annoncé, les données publiques sur le sujet et les évaluations indépendantes disponibles. Elle conserve les sources précises, les dates de première et dernière observation, le statut de la proposition et les limites des vérifications effectuées par IA. L’index du candidat relie chaque fiche à son domaine et à une courte description factuelle.

## Langue

La langue du dépôt est le français. Les contributions et la documentation sont rédigées en français.

## Structure

- `AGENTS.md` : règles de travail et de réponse pour les assistants.
- `METHODOLOGIE.md` : principes de collecte, de vérification et de comparaison.
- [Guides par domaine](guides/README.md) : socle commun et 22 guides de vérification, avec données à rechercher, contrôles et sources de départ.
- [Repérage 2017–2022](guides/reperage-2017-2022.md) : origine du découpage et limites de la recherche historique.
- `candidats/` : un dossier par candidat avec un `README.md` d’index (domaine, mini-description et lien), puis une fiche par mesure.
- `modeles/candidat.md` : modèle d’index par candidat.
- `modeles/mesure.md` : modèle commun de fiche.
- `sources/` : base commune de références institutionnelles, répertoire des producteurs et documents de tiers avec notices de droits.
- `modeles/reference.md` : modèle de fiche pour un indicateur ou une publication.

## Candidats suivis

Le corpus suit volontairement une **liste restreinte** pendant la phase préparatoire, avec pour repère environ **5 % ou davantage atteints au moins une fois dans un sondage national de premier tour pour 2027**, à documenter dans chaque dossier. Ce choix sert à concentrer les moyens de collecte ; il ne constitue ni un classement de qualité ni un jugement sur la légitimité des autres candidatures. Les sondages restent des estimations, pas une garantie de résultat ou de candidature.

La liste sera complétée à mesure que les candidatures se préciseront. Les candidatures suivies doivent être annoncées et confirmées par des sources primaires ; les personnes seulement pressenties sont exclues. Dès publication de la liste officielle, seuls les candidats retenus restent suivis. Les dossiers des personnes qui renoncent ou ne sont pas retenues sont retirés du corpus courant ; leur historique Git est conservé. Voir les critères et modalités dans la [méthodologie](METHODOLOGIE.md#sélection-initiale-et-élargissement).

## Réutilisation

Les contenus originaux du projet sont placés sous **CC0 1.0 Universel** : réutilisation, modification et redistribution, y compris commerciale, sans obligation d’attribution dans la mesure permise par cet instrument. Voir la [licence et son périmètre](LICENSE.md) pour les exclusions concernant les contenus de tiers. Le dépôt peut contenir des éléments de tiers sous d’autres conditions, explicitement identifiés ; il n’est pas intégralement sous CC0. La conservation des références est recommandée pour permettre la vérification, sans constituer une condition supplémentaire à CC0.

## Production par IA

Le corpus est collecté, rédigé et contrôlé par IA, sans relecture humaine. Les contrôles effectués et leurs limites sont documentés ; des erreurs peuvent subsister. Un contrôle documentaire ne valide pas automatiquement les déclarations rapportées.

## Contribuer

Lire la méthodologie et les consignes avant toute contribution. Chaque ajout doit être sourcé et daté. L’état de contrôle documentaire par IA est distinct de la vérification du fond de chaque affirmation. En contribuant, ne placer sous CC0 que des contenus sur lesquels vous détenez les droits nécessaires. Les corrections doivent conserver la trace des changements substantiels.

## Rafraîchir un programme avec un assistant

Ouvrir la **racine du dépôt cloné** dans Codex, Claude Code ou le mode Agent de Cursor, puis démarrer une nouvelle conversation. La procédure est entièrement décrite dans le dépôt ; elle ne dépend pas de la conversation qui a servi à le créer.

| Assistant | Entrée des consignes | Parcours de rafraîchissement |
| --- | --- | --- |
| Codex | [AGENTS.md](AGENTS.md) | Skill local dans `.agents/skills/rafraichir-programme/`, puis [procédure commune](procedures/rafraichir-programme.md). |
| Claude Code | [CLAUDE.md](CLAUDE.md), qui importe `AGENTS.md` | Les règles communes déclenchent la même procédure sur une demande en français ; aucun skill Claude séparé n’est nécessaire. |
| Cursor, mode Agent | `AGENTS.md` ; skill partagé dans `.agents/skills/` sur les versions qui le prennent en charge | Même procédure ; le texte de `AGENTS.md` fournit aussi le chemin si le skill n’est pas détecté. |

Demande simple :

> Rafraîchis le programme de Mélenchon.

Pour rendre le démarrage explicite, notamment avec un autre assistant :

> Lis AGENTS.md et applique procedures/rafraichir-programme.md pour rafraîchir le programme de Jean-Luc Mélenchon jusqu’à la mise à jour des fiches et de son index. Respecte la recherche indépendante, les guides par domaine et l’isolation par candidat.

### Prérequis et premier démarrage

- Autoriser l’assistant à lire et modifier ce clone, à consulter le Web et à exécuter le script local de préparation. Les permissions restent celles du client ; le dépôt ne les modifie pas.
- Le script utilise Python 3.9 ou plus récent et les données de fuseau `Europe/Paris`. Il utilise uniquement la bibliothèque standard : PyYAML n’est pas nécessaire au rafraîchissement. Si Python ou le fuseau manque, le signaler avant d’installer quoi que ce soit ; la préparation manuelle équivalente est décrite dans la procédure.
- Les espaces `_travail/` sont recréés localement et restent ignorés par Git. Les dossiers vides `mesures/` et `sources/references/` peuvent être absents d’un clone : les créer lors de leur première utilisation, sans interpréter cette absence comme une suppression de contenu.
- Pour plusieurs candidats, employer des agents distincts. Si le client ne le permet pas, utiliser des conversations indépendantes, une par candidat ; ne pas enchaîner plusieurs candidats dans le même agent de contenu.
- Aucun serveur MCP propre au projet ni accès à la machine de l’auteur n’est requis. Les outils de navigation du client suffisent s’ils permettent de consulter les sources ; les accès bloqués doivent être signalés.

Les formats de découverte ont été contrôlés dans les documentations officielles le 2026-10-15 : [Codex — instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex — skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code — import de consignes](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools), [Cursor — règles](https://cursor.com/docs/rules) et [Cursor — skills](https://cursor.com/help/customization/skills). Les réglages personnels peuvent désactiver ces mécanismes ; en cas de doute, demander à l’assistant de nommer les fichiers d’instructions chargés avant de commencer.

La compatibilité porte sur les points d’entrée et la procédure commune. Les instructions ne garantissent pas une exécution sans erreur et ne constituent pas un contrôle logiciel bloquant de toutes les règles. Un rafraîchissement complet doit être vérifié dans le client utilisé ; ne pas confondre validation des fichiers, test du script et exécution réelle par un agent.

La procédure collecte d’abord les éléments bruts dans un espace `_travail/` propre au candidat, ignoré par Git, puis applique les guides pertinents pour rechercher les données publiques et analyses indépendantes avant de consolider les fiches et leur index. Une demande de collecte seule s’arrête avant consolidation. Les modèles modestes sont privilégiés pour limiter les coûts. Aucun rafraîchissement automatique périodique n’est lancé.

Un rafraîchissement comprend l’application des décisions de consolidation dans les fiches et l’index du candidat. Chaque agent de contenu travaille sur un seul candidat ; pour trois candidats, utiliser au moins trois agents distincts. Un coordinateur peut répartir les travaux et rassembler leurs bilans sans mélanger les contenus.

Avant la consolidation finale, chaque mesure fait l’objet d’une recherche de données publiques et d’analyses indépendantes auprès des références du dépôt et des producteurs pertinents. La fiche présente le contexte public, les éléments comparables et les limites ; une recherche infructueuse est signalée explicitement.
