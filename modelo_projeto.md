








Dossier de Projet
Titre professionnel : Concepteur Développeur d’Applications

 










 
Sommaire
Préface & Remerciements	3
1. Introduction et présentation du projet Izilife	4
1.1. Parcours personnel et origine du projet	4
1.2. Objectifs et valeurs d’IziLife	4
1.3. Présentation synthétique de la plateforme	5
1.4. Publics cibles	6
2. Conception du projet	7
2.1. Expression des besoins par type d’utilisateur	7
2.2. User Stories	7
2.3. Règles de gestion métier	9
2.4. Parcours utilisateurs & maquettes Figma	11
2.5. Conception de la base de données	12
2.6. Diagrammes UML	14
2.7. Architecture logicielle (organisation du code, services, types métiers)	15
2.8. Méthodologie agile (Scrum, Sprints, Trello, outils utilisés)	17
3. Développement	19
3.1. Stack technique	19
3.2. Extraits de code commentés	20
3.3. Sécurité de l’application	27
3.4. Accessibilité numérique (WCAG, RGAA)	28
3.5. Écoconception (optimisations front/back, performances)	30
3.6. Tests & validation	31
4. Déploiement et CI/CD	32
4.1. Conteneurisation avec Docker	32
4.2. Pipeline GitLab CI/CD	33
4.3. Hébergement sur serveur Vultr	34
4.4. Supervision et maintenance (Portainer, logs, backups)	35
4.5. Sécurité et conformité en production	36
5. Bilan et améliorations futures	38
5.1. Bilan personnel et professionnel	38
5.2. Compétences mobilisées	38
5.3. Fonctionnalités et extensions prévues	40
5.4. Pistes d’optimisation technique et UX	40
5.5. Perspectives post-certification	42
6. Annexes	43
Préface & Remerciements
Ce dossier est l’aboutissement d’un projet profondément personnel et formateur. IziLife ne représente pas uniquement la validation d’un titre professionnel, mais aussi une manière de mettre mes compétences au service d’une cause qui me touche : celle de l’inclusion et de l’accessibilité numérique.
Je tiens à remercier chaleureusement toutes les personnes qui ont contribué, de près ou de loin, à rendre ce parcours aussi enrichissant qu’humain :
●	Mes camarades de promo, pour l’entraide constante, les partages de galères comme de victoires, et le soutien collectif qui a rendu cette aventure formatrice… et surtout jamais ennuyeuse.

●	Renaud et Nicolas, nos formateurs, pour leur bonne humeur, leur humour et leur pédagogie, même face à mes nombreuses questions. Merci pour votre patience et vos encouragements.

●	Léopoldine, notre chargée de promo, pour son soutien, sa disponibilité, son sourire, et sa bienveillance naturelle.

●	Julien, Arnaud et Guillaume, les dirigeants de Dev-ID, pour m’avoir accordé leur confiance et offert l’opportunité d’effectuer mon alternance dans un cadre unique : un vrai compagnonnage moderne qui m’a énormément appris, tant techniquement qu’humainement.

●	Nacer, Malik et Yoann, mes maîtres de compagnonnage chez Dev-ID, pour le temps qu’ils m’ont consacré, leur écoute attentive, leurs explications claires et leurs retours toujours pertinents. J’ai beaucoup appris grâce à vous.

●	Et bien sûr, toute l’équipe Dev-ID, pour l’ambiance saine, le respect mutuel, les moments de détente comme les projets sérieux. Travailler dans cette équipe est un plaisir quotidien, et je mesure la chance que j’ai de pouvoir m’y épanouir pleinement.

Enfin, je remercie celles et ceux qui m’ont encouragé, soutenu et challengé durant ce projet. Ce parcours m’a permis d’affirmer encore un peu plus ma vision du métier : celle d’un développeur engagé, rigoureux, mais aussi profondément humain.
 
1. Introduction et présentation du projet Izilife
 
1.1. Parcours personnel et origine du projet
Étant moi-même en situation de handicap moteur depuis la naissance, j’ai grandi et évolué dans un environnement « ordinaire », en dehors des structures spécialisées. Ce contexte m’a offert beaucoup d’opportunités, mais il m’a aussi longtemps tenu à distance d’un élément essentiel : le partage d’expériences entre personnes vivant des réalités similaires.
Ce manque est devenu évident lors d’un séjour en centre de rééducation fonctionnelle. En quelques semaines, j’y ai découvert une richesse insoupçonnée : astuces concrètes, techniques du quotidien, recommandations d’objets et de services adaptés… autant de connaissances précieuses que je n’avais jamais croisées auparavant. J’ai alors réalisé combien ce savoir partagé pouvait transformer le quotidien.
C’est ainsi qu’est née l’idée d’IziLife : une plateforme numérique collaborative, pensée pour centraliser ces solutions, faciliter les échanges entre personnes concernées, et valoriser cette intelligence collective souvent dispersée.
Ce projet est pour moi l’occasion de lier mes compétences techniques, développées dans le cadre de la formation CDA, à mon engagement personnel pour l’inclusion et l’accessibilité. IziLife est à la fois un défi professionnel et un prolongement de mon parcours de vie.
 
1.2. Objectifs et valeurs d’IziLife
IziLife est né d’un besoin simple : créer un espace où les personnes en situation de handicap peuvent partager leurs solutions, s’entraider, et accéder plus facilement à des informations utiles pour leur quotidien.
L’objectif principal est de centraliser des contenus pratiques, issus de l’expérience réelle des utilisateurs : objets adaptés, services accessibles, lieux recommandés, mais aussi discussions et conseils. En rendant cette richesse collective visible et accessible à tous, IziLife vise à éviter que chacun ne doive réinventer seul des réponses déjà trouvées ailleurs.
Au-delà de sa fonction de plateforme, IziLife incarne des valeurs fondamentales qui ont guidé chaque étape de son développement :
●	Inclusivité : une plateforme pensée pour tous les profils d’utilisateurs, quels que soient leurs besoins ou leurs contraintes.

●	Accessibilité numérique : le respect des standards WCAG et RGAA est intégré dès la conception pour garantir une expérience fluide et équitable.

●	Partage et entraide : les contenus sont créés par la communauté, pour la communauté, dans une logique d’échange désintéressé.

●	Innovation utile : les fonctionnalités techniques sont orientées vers des usages concrets, simples et adaptés aux besoins réels.

●	Respect et sécurité : les données personnelles sont protégées, et l’environnement est modéré pour garantir un cadre serein.

IziLife se veut donc à la fois un outil pratique, un vecteur d’autonomie, et un espace communautaire porteur de sens.
 
1.3. Présentation synthétique de la plateforme
IziLife est une plateforme collaborative destinée aux personnes en situation de handicap, à leurs proches et aux professionnels concernés. Son objectif est de permettre à chacun de partager, consulter et commenter des solutions concrètes pour faciliter le quotidien.
Les utilisateurs peuvent y publier des solutions sous forme d’objets, de services ou de lieux accessibles, accompagnées d’une description, d’un prix, d’une URL et d’images. Chaque solution peut être associée à une ou plusieurs catégories de handicap.
La plateforme propose également un espace de discussions thématiques, organisé par grandes catégories (accessibilité, santé, vie quotidienne, etc.), dans lequel les membres peuvent poser des questions, partager leurs retours d’expérience et échanger librement.
Solutions et discussions peuvent être commentées, ajoutées en favoris, aimées ou signalées. Un système de modération permet de garantir la qualité et la sécurité des contenus publiés.
IziLife fonctionne comme une véritable communauté numérique d’entraide, accessible via une interface simple, inclusive et responsive.
 
1.4. Publics cibles
IziLife s’adresse à plusieurs types d’utilisateurs, aux profils et besoins variés, mais tous concernés par la recherche de solutions concrètes liées au handicap. Pour mieux cerner ces publics, trois personas représentatifs ont été créés.
Fabien, 26 ans, est paraplégique depuis un accident de la vie quotidienne. Il vit chez ses parents, travaille à distance, et cherche à retrouver son autonomie. Passionné de sport, il aimerait intégrer un club de basket-fauteuil mais manque d’outils pour démarrer. Il a besoin d’une plateforme qui centralise des solutions concrètes, accessibles et récentes pour organiser sa nouvelle vie.
Sabrina, 40 ans, est aidante professionnelle. Elle accompagne Théo, un jeune atteint de myopathie de Duchenne, depuis plusieurs années. Malgré son expérience, elle se heurte à un manque de ressources fiables. Elle aimerait trouver un espace pour échanger avec d’autres aidants, repérer du matériel adapté, et bénéficier d’une interface claire et facile à utiliser, même sans compétences informatiques avancées.
Christie, 38 ans, est conseillère dans une association spécialisée. Elle accompagne de nombreuses personnes en situation de handicap et leurs familles. Face à la diversité des besoins, elle souhaite disposer d’un outil fiable et personnalisable pour recommander des solutions selon le profil de chaque personne accompagnée.
Ces exemples illustrent la diversité des utilisateurs visés par IziLife, qui peut également concerner :
●	des familles ou proches en quête d’informations pratiques ;

●	des professionnels du secteur médico-social ou éducatif ;

●	des citoyens sensibles aux enjeux d’accessibilité et d’inclusion.

L’interface d’IziLife a donc été pensée pour répondre à ces profils variés, avec une navigation intuitive, des filtres par catégorie de handicap, et une logique de partage d’expérience favorisant l’entraide.
 
2. Conception du projet
 
2.1. Expression des besoins par type d’utilisateur
Le projet IziLife repose sur une plateforme pensée pour plusieurs profils d’utilisateurs. Chaque type d’utilisateur exprime des besoins spécifiques, que j’ai pris en compte dans la conception fonctionnelle et technique de l’application.
Personnes en situation de handicap
Elles ont besoin de découvrir rapidement des solutions concrètes adaptées à leur situation : objets du quotidien, services utiles, lieux accessibles, ou astuces partagées par d’autres. Elles souhaitent aussi pouvoir publier leurs propres retours d’expérience, interagir avec d’autres membres, et se sentir intégrées à une communauté bienveillante.
Aidants familiaux ou professionnels
Ils cherchent un espace centralisé et fiable pour trouver du matériel adapté, des recommandations concrètes, des conseils pratiques. Ils ont besoin d’une interface claire, simple à utiliser, qui ne nécessite pas de connaissances techniques, et qui leur permette d’échanger entre pairs.
Professionnels de l’orientation ou de l’accompagnement social
Ils accompagnent une grande diversité de situations et ont besoin d’un outil de veille et de recommandation rapide. Ils souhaitent pouvoir orienter efficacement les bénéficiaires vers des ressources pertinentes, à jour, et classées selon les types de handicaps.
Autres utilisateurs sensibles à l’accessibilité
Certains usagers, bien qu’indirectement concernés, peuvent souhaiter contribuer à la plateforme : citoyens engagés, commerçants, développeurs ou responsables de lieux publics. Ils ont besoin d’un espace pour partager des initiatives, découvrir des bonnes pratiques, ou soutenir la démarche inclusive d’IziLife.
 
2.2. User Stories
Les fonctionnalités d’IziLife ont été définies à partir des besoins exprimés par les différents types d’utilisateurs. Chaque besoin a été transformé en User Story claire, priorisée et intégrée dans un backlog structuré en sprints.

Voici une sélection représentative des User Stories développées.
Utilisateur connecté – publication et interaction
●	En tant qu’utilisateur, je veux publier une solution avec description, type, prix, images et catégories, afin de la partager avec la communauté.

●	En tant qu’utilisateur, je veux créer une discussion pour poser une question ou échanger un retour d’expérience.

●	En tant qu’utilisateur, je veux commenter une solution ou une discussion afin de contribuer aux échanges.

●	En tant qu’utilisateur, je veux pouvoir signaler un contenu inapproprié pour garantir un espace respectueux.

Utilisateur connecté – navigation et personnalisation
●	En tant qu’utilisateur, je veux rechercher des solutions par catégorie, type ou mot-clé afin de trouver celles qui me concernent.

●	En tant qu’utilisateur, je veux enregistrer des solutions ou discussions en favoris pour les retrouver facilement.

●	En tant qu’utilisateur, je veux indiquer que j’aime un contenu afin de soutenir les contributions utiles.

Utilisateur non connecté (visiteur)
●	En tant que visiteur, je veux consulter les solutions et discussions validées afin de découvrir le contenu public du site.

●	En tant que visiteur, je veux pouvoir m’inscrire pour interagir avec la communauté.





Administrateur
●	En tant qu’administrateur, je veux modérer les signalements reçus pour valider ou supprimer les contenus concernés.

●	En tant qu’administrateur, je veux gérer les catégories de handicap et de discussion afin de structurer les contenus publiés.

●	En tant qu’administrateur, je veux pouvoir bannir ou réactiver un utilisateur en cas d’abus.

Notification et feedback utilisateur
●	En tant qu’utilisateur, je veux recevoir une notification lorsqu’un de mes contenus est commenté ou modéré.

●	En tant qu’utilisateur, je veux être informé du succès ou de l’échec de mes actions (inscription, publication, etc.).

L’ensemble des User Stories est classé par sprint dans la partie 2.8 (méthodologie agile) et détaillé intégralement en annexe (cf. p. 47-59).
 
2.3. Règles de gestion métier
L’application IziLife repose sur un ensemble de règles métier qui garantissent la cohérence fonctionnelle, la sécurité des échanges et la fluidité de l’expérience utilisateur. Ces règles ont été définies dès la phase de conception et sont appliquées côté front et back.
Gestion des statuts utilisateur
●	Un utilisateur a un statut parmi pending, active, ou banned.

●	Un utilisateur avec le statut pending peut se connecter mais ne peut pas publier ou interagir tant que son adresse mail n’a pas été confirmée.

●	Un utilisateur banned ne peut plus se connecter.

Publication de contenus
●	Seuls les utilisateurs active peuvent publier des solutions ou des discussions.

●	Toute publication est créée avec un statut pending et doit être validée par un administrateur avant d’être visible publiquement.

●	Une solution ou une discussion validée passe en statut published.

Signalement et modération
●	Tout contenu peut être signalé par un utilisateur authentifié, une seule fois par contenu.

●	Le signalement nécessite un motif obligatoire (enum ReportReason) et peut être accompagné d’un commentaire.

●	L’administrateur traite chaque signalement en appliquant une action de modération (approve, hide, delete).

Commentaires
●	Les utilisateurs peuvent commenter une solution ou une discussion, ou répondre à un commentaire (5 niveaux de profondeur).

●	Les commentaires peuvent être modifiés ou désactivés par leur auteur.

●	Un commentaire supprimé est marqué comme “commentaire désactivé”, mais reste visible dans le fil.

Gestion des images
●	L’utilisateur peut envoyer jusqu’à 8 images par solution, dont une image principale.

●	Les formats acceptés sont restreints (PNG, JPG, WebP).

●	Les fichiers sont automatiquement compressés côté serveur avant d’être stockés sur MinIO.


Catégorisation des contenus
●	Une solution est liée à un ou plusieurs types de handicap.

●	Une discussion est liée à une seule catégorie de discussion, et éventuellement à des types de handicap.

●	Les catégories sont créées et gérées par les administrateurs.

Ces règles garantissent à la fois la qualité des contenus, la modération efficace, la simplicité d’usage pour les utilisateurs, et la structure claire des données côté base.
 
2.4. Parcours utilisateurs & maquettes Figma
Avant de développer l’application, j’ai commencé par concevoir les parcours utilisateurs pour répondre aux besoins identifiés lors de l’analyse fonctionnelle. Cette étape a permis de clarifier les écrans nécessaires, la logique de navigation, et les points de friction à éviter.
Parcours utilisateur principal
Le parcours le plus central est celui d’un utilisateur connecté qui souhaite publier une solution. Il comprend les étapes suivantes :
1.	Connexion au compte (ou inscription si nouveau compte)

2.	Accès au formulaire de création de solution

3.	Remplissage des champs (url, titre, description, type, prix, catégories de handicap)

4.	Upload des images avec définition de l’image principale

5.	Validation finale et envoi

6.	Message de confirmation (contenu en attente de validation)



D’autres parcours secondaires ont été modélisés pour :
●	La recherche de solutions par filtres

●	La consultation des discussions

●	L’interaction (likes, favoris, commentaires)

●	La gestion du profil utilisateur

●	Le signalement et la modération des contenus

Travail de maquettage
L’ensemble des écrans a été conçu sur Figma, avec une attention particulière portée :
●	à l’accessibilité (contrastes, tailles de texte, navigation clavier)

●	à la cohérence graphique (UI unifiée)

●	à la clarté des formulaires et des retours utilisateurs
Les maquettes ont été réalisées dans une logique mobile-first, puis adaptées en version desktop. Elles ont servi de base tout au long du développement frontend.
Les maquettes Figma sont présentées dans les annexes (cf. p. 64-66).
 
2.5. Conception de la base de données
La base de données d’IziLife a été conçue selon une approche relationnelle, avec une forte structuration des types métier. Elle a été modélisée à l’aide de diagrammes MCD et MLD sur Eraser, puis implémentée avec Prisma en tant qu’ORM dans l’application NestJS.
Étapes de conception
1.	MCD (Modèle Conceptuel de Données)
Le MCD a permis de poser les grandes entités : utilisateurs, solutions, discussions, commentaires, images, catégories, signalements, notifications, etc., ainsi que les associations entre elles et leurs cardinalités.

2.	MLD (Modèle Logique de Données)
Le MLD a détaillé les types d’associations (1-N, N-N), les clés primaires et étrangères, et les attributs métiers. Une attention particulière a été portée à :

○	La séparation claire entre solutions et discussions, tout en unifiant les interactions (likes, favoris, commentaires)

○	Le stockage des images (image principale + images secondaires)

○	La gestion des statuts (published, pending, disabled) sur tous les contenus

○	La centralisation des signalements dans une table commune (ContentModeration) avec enums typés

3.	MPD (Modèle Physique via Prisma)
 Le modèle a ensuite été transformé en schéma Prisma, avec :

○	Définition explicite des types (enum, @relation, @default, etc.)

○	Gestion des migrations (prisma migrate dev et migrate deploy)

○	Synchronisation automatique avec PostgreSQL en développement et en production

Cohérence avec la logique applicative
●	Tous les types métiers (statuts, rôles, types de solution, types de catégorie, motifs de signalement…) sont définis à la fois dans la base et dans le code TypeScript, assurant une cohérence stricte du système.

●	Les associations many-to-many (ex : solutions ↔ catégories, utilisateurs ↔ favoris) sont gérées via des tables d’associations explicites.

●	Les suppressions sont logiques ou physiques en fonction de la nécessité de préserver un historique (les commentaires par exemple).

Les schémas MCD (cf. p. 44) et MLD (cf. p. 45) sont présentés en annexe.
 
2.6. Diagrammes UML
Afin de formaliser les principales interactions dans l’application IziLife, j’ai réalisé plusieurs diagrammes UML à différentes étapes du projet. Ces schémas m’ont aidé à clarifier les rôles des utilisateurs, le déroulement des actions clés, et l’organisation interne des objets manipulés.
Diagramme de cas d’utilisation
Ce diagramme représente les actions possibles pour chaque type d’utilisateur : visiteur, utilisateur connecté, administrateur. Il permet de visualiser les frontières du système, les fonctionnalités accessibles selon les rôles, et les cas spécifiques comme la modération ou la gestion des catégories.
Les cas d’utilisation modélisés incluent :
●	Inscription, connexion, gestion du profil

●	Publication et consultation de solutions ou discussions

●	Signalement de contenus

●	Modération par un administrateur

●	Actions communautaires (likes, favoris, commentaires, signalements)

Diagramme de séquence
J’ai modélisé en détail le processus de publication d’une solution, depuis l’action utilisateur jusqu’à la création en base de données et l’upload des images dans MinIO.
Le diagramme permet de suivre les interactions entre :
●	Le frontend React (formulaire multi-étapes)

●	Le backend NestJS (contrôleur, service, repository)

●	Le service MinIO pour le stockage

●	La base de données via Prisma

Cette modélisation m’a permis de structurer mon code en couches distinctes et d’anticiper les validations nécessaires à chaque étape.
Les différents diagrammes UML sont consultables dans les annexes (cf. p. 60-63).
 
2.7. Architecture logicielle (organisation du code, services, types métiers)
L’architecture logicielle d’IziLife a été pensée pour garantir la lisibilité, la maintenabilité et la modularité du projet. Elle repose sur une organisation claire, tant côté back-end que front-end, avec une séparation des responsabilités rigoureuse.
Côté back-end (NestJS)
L’application back-end est développée avec NestJS et structurée en modules fonctionnels (auth, users, solutions, discussions, etc.). Chaque module regroupe :
●	Un contrôleur (*.controller.ts) : gestion des routes

●	Un service (*.service.ts) : logique métier

●	Un repository (*.repository.ts) : abstraction de l’accès à la base via Prisma

●	Des DTOs (*.dto.ts) : validation des entrées

●	Des mappers (*.mapper.ts) : conversion entre entités et réponses API
L’accès à la base est centralisé via PrismaService, et les services transverses (MinIO, mails, notifications) sont injectés via le système d’injection de dépendances NestJS.
L’arborescence suit une logique modulaire :
src/
├── solutions/
│   ├── solutions.controller.ts
│   ├── solutions.service.ts
│   ├── solutions.repository.ts
│   ├── solutions.mapper.ts
│   ├── solutions.module.ts
│   └── dto/
├── discussions/
├── users/
├── moderation/
├── auth/
├── mails/
├── minio/
└── prisma/

Côté front-end (React + Vite)
L’application front est développée en React avec TypeScript, selon une architecture par domaine fonctionnel :
●	components/ : composants UI réutilisables et spécifiques

●	pages/ : pages liées aux routes de l’application

●	hooks/ : logique métier réutilisable (auth, solutions, discussions…)

●	stores/ : gestion d’états via Zustand

●	lib/api/ : appels API typés par domaine

●	types/ : définitions TypeScript centralisées

●	config/ : constantes et paramètres globaux

L’organisation du front vise la clarté, la réutilisabilité des composants, et l’isolation de la logique métier dans des hooks dédiés.
Types métiers et enums
L’ensemble des rôles (user, admin), statuts (pending, active, banned, published, disabled), types de contenus (solution, discussion, comment), catégories et motifs de signalement sont définis dans des enums partagés et synchronisés avec la base via Prisma.
Cela garantit une cohérence forte entre la couche base, l’API, et l’interface utilisateur.
 
2.8. Méthodologie agile (Scrum, Sprints, Trello, outils utilisés)
Le développement d’IziLife a suivi une démarche agile inspirée du framework Scrum, avec une planification par sprints, un backlog priorisé, et un suivi continu des tâches. Cette organisation m’a permis de structurer efficacement le travail, d’itérer rapidement et d’adapter le développement aux contraintes de temps.
Découpage en sprints
Le projet a été découpé en 10 sprints thématiques, chacun durant deux semaines. Chaque sprint avait des objectifs précis et regroupait des User Stories cohérentes par fonctionnalité ou par enjeu technique (cf. p. 58-59).
1.	Maquettage UX/UI
Travail sur Figma, définition des parcours utilisateurs, validation des maquettes.

2.	Environnement technique & Authentification
Mise en place du projet (front et back), gestion des utilisateurs et sécurité.

3.	Gestion des contenus
Création de solutions et discussions, structuration des entités métiers.

4.	Consultation & filtrage
Recherche de solutions et discussions, visualisation du détail d’un contenu.

5.	Fonctionnalités communautaires & signalement
Likes, commentaires, favoris, signalements, modification de contenus.

6.	Tableau de bord administrateur + notifications
Interface admin, gestion des signalements, notifications, modération utilisateur.

7.	Tests, sécurité & accessibilité
Tests manuels et E2E, contrôle d’accessibilité, validations back.

8.	Déploiement Docker & CI/CD
Dockerisation, création du pipeline GitLab, supervision via Portainer.

9.	Finalisation, documentation & optimisation
Nettoyage du code, documentation technique, optimisations front/back.

10.	Améliorations continues
Roadmap post-projet, idées d’extension, feedback utilisateurs.

Suivi de projet avec Trello
J’ai utilisé Trello comme tableau de bord visuel. Chaque User Story y était représentée par une carte, classée par sprint et étiquetée selon le domaine (auth, front, back, admin, etc.).
Les cartes incluaient :
●	La description de l’US

●	Les critères d’acceptation
Trello m’a permis de maintenir une vision claire de l’avancement et de prioriser efficacement les tâches.
Outils utilisés
●	Figma : maquettage UI/UX et organisation des parcours utilisateurs

●	GitLab : versionning, CI/CD

●	Postman : tests API

●	Eraser, mocodo & dbdiagram : MCD, MLD, diagrammes UML

●	Portainer : supervision des conteneurs Docker en production

●	Cursor (IDE) : développement front/back avec intégration AI

 
 
3. Développement
 
3.1. Stack technique
Le projet IziLife a été développé en fullstack TypeScript, avec une stack moderne, modulaire et orientée production. Chaque technologie a été choisie pour sa robustesse, sa compatibilité avec l’accessibilité et sa capacité à s’intégrer dans une architecture conteneurisée.
Front-end
L’interface utilisateur est développée avec React (via Vite) et structurée autour de composants typés avec TypeScript. Le front utilise :
●	React Hook Form + Zod pour les formulaires et la validation

●	TanStack Query pour la gestion des données côté client (cache, chargement, erreurs)

●	Zustand pour la gestion des states

●	Une architecture modulaire par domaine (auth, solutions, discussions…)

Back-end
L’API est développée en NestJS avec :
●	Une structure en modules fonctionnels

●	Des DTOs pour la validation, des services métier clairs, et des guards pour l’authentification et l’autorisation d’accès en fonction du rôle

●	L’ORM Prisma, connecté à une base PostgreSQL, avec gestion fine des relations et des enums métiers

●	Des services transverses : gestion des emails (SMTP Ionos), envoi d’images (MinIO)


Infrastructure
Le projet est entièrement conteneurisé avec Docker :
●	Front et back ont chacun un Dockerfile dédié (cf. p. 66-67)

●	La stack est orchestrée via Docker Compose (cf. p. 68)

●	Le reverse proxy Nginx gère le routage et le HTTPS (Let’s Encrypt) (cf. p. 71)

●	Le déploiement est assuré sur un VPS Vultr, avec supervision via Portainer

Cette stack m’a permis de construire une plateforme fiable, accessible, sécurisée et facile à maintenir.
 
3.2. Extraits de code commentés
Pour illustrer concrètement le fonctionnement d’une fonctionnalité clé d’IziLife, je présente ici la chaîne complète de publication d’une solution, du front-end à la base de données, en passant par la gestion des fichiers et la sécurisation des données.
Cette fonctionnalité reflète à la fois la rigueur de la structure modulaire, la séparation des responsabilités, la gestion fine des types et la logique orientée utilisateur.
Le processus se déroule en plusieurs étapes que je vais présenter avec les extraits de code correspondants.







1.	Formulaire multi-étapes en React (ManageSolutionDialog.tsx)
L’utilisateur remplit le formulaire de manière progressive : lien, informations, images, récapitulatif. Chaque étape est isolée, avec un état centralisé (formData) partagé. À la fin du parcours, les données et les fichiers sont transmis à l’API via une mutation personnalisée.

2.	Mutation côté front (useCreateSolution.ts)
La mutation utilise TanStack Query pour envoyer le formData et gérer la mise à jour automatique du cache. En cas d’erreur ou de succès, un retour visuel est proposé à l’utilisateur.




3.	Appel API (solutions.api.ts)
Les données et les fichiers sont transformés en multipart/form-data, puis envoyés vers l’endpoint d’upload. Les images sont ajoutées une par une au FormData, les catégories sont sérialisées, et l’image principale est identifiée.

4.	Contrôleur NestJS (solutions.controller.ts)
L’endpoint POST /solutions/create est sécurisé par un guard JWT. Il reçoit le corps de la requête (CreateSolutionDto) et les fichiers (via Multer). Ces éléments sont transférés au service principal.
5.	Service NestJS (solutions.service.ts)
Le service commence par valider l’URL si elle est présente, puis lance une transaction Prisma. Les images sont d’abord traitées via le service MinIO, puis la solution est enregistrée en base avec toutes ses relations (catégories, images…).
6.	Service MinIO (minio.service.ts)
Chaque image est renommée proprement, compressée (Sharp), convertie en WebP, puis envoyée vers MinIO. L’URL est ensuite renvoyée au service appelant pour être sauvegardée.
7.	Création en base via Prisma (solutions.repository.ts)
La solution est créée avec ses données textuelles, ses images (avec l’attribut is_main), ses catégories (via relations connect), et un retour enrichi est généré (pseudo auteur, image profil…).
Chaque étape est typée strictement et isolée dans une couche dédiée. Ce fonctionnement démontre l’efficacité de l’architecture mise en place et sa capacité à évoluer proprement.
 
3.3. Sécurité de l’application
La sécurité a été intégrée à chaque niveau du développement d’IziLife, aussi bien dans l’architecture back-end que dans l’authentification, la gestion des permissions, le traitement des données utilisateurs et les accès en production.
Authentification et autorisation
●	L’authentification est basée sur JWT, avec access token court et refresh token stocké côté client.

●	Les routes sensibles sont protégées par des guards NestJS (@Protect()), qui vérifient le rôle et l’état du compte (active uniquement).

●	Les administrateurs disposent d’un accès étendu avec l’accès aux fonctionnalités de modération et de gestion.

Sécurisation des données utilisateur
●	Les mots de passe sont hashés avec bcrypt côté serveur.

●	Les adresses email doivent être confirmées pour débloquer l’accès aux fonctionnalités sociales (publication, commentaire, etc.).

●	Les rôles, statuts et types métiers sont strictement typés via des enums partagés entre Prisma et NestJS.

Validation et protection côté back
●	Toutes les données entrantes sont validées via des DTOs décorés avec class-validator et class-transformer.

●	Aucun champ non prévu n’est accepté, et chaque requête passe par un pipe de validation global.

●	Le système de signalement utilise une table dédiée (ContentModeration) et n’autorise qu’un signalement par utilisateur et par contenu.

Sécurité des fichiers et des images
●	Seuls certains formats sont acceptés à l’upload (JPG, PNG, WebP).

●	Les fichiers sont renommés, compressés et convertis via Sharp avant stockage dans MinIO.

●	Les URL d’accès aux images sont générées de manière contrôlée, sans injection de nom brut.

Sécurité en production
●	Le serveur est protégé par SSH avec clé privée uniquement.

●	Toutes les communications passent par HTTPS (certificats Let’s Encrypt).

●	L’accès à Portainer est restreint, et aucun conteneur interne n’est exposé sans proxy Nginx.

●	Les secrets (JWT, SMTP, variables Prisma) sont stockés dans un fichier .env hors dépôt et injectés via GitLab CI.

Ce socle sécurisé garantit la protection des données, le respect des bonnes pratiques, et un cadre d’utilisation stable pour les utilisateurs finaux.
 
3.4. Accessibilité numérique (WCAG, RGAA)
L’accessibilité fait partie des valeurs fondatrices du projet IziLife. Elle a été intégrée dès la conception des maquettes, puis tout au long du développement. L’objectif était de garantir une navigation inclusive pour tous les utilisateurs, quels que soient leurs besoins ou leurs capacités.


Approche adoptée
●	Les maquettes Figma ont été pensées mobile-first, avec des contrastes suffisants, une hiérarchie claire de l’information, et une navigation cohérente.

●	Les composants React sont tous accessibles au clavier, avec gestion des focus, des messages d’erreur et des retours visuels explicites.

●	Les balises HTML sémantiques sont correctement utilisées (section, nav, main, h1…).

●	Les champs de formulaire sont tous associés à un label explicite.

●	Les icônes décoratives sont cachées des lecteurs d’écran (aria-hidden), et les images porteuses d’information disposent d’un attribut alt.

Résultats obtenus
Un audit automatique avec Lighthouse a permis d’obtenir les scores suivants sur la version de production :
 
Des tests manuels ont également été effectués avec la navigation clavier seule (sans souris), pour valider l’ordre de tabulation, les focus visuels, et le fonctionnement des formulaires.
Limites
Par manque de temps, certaines vérifications avancées n’ont pas pu être mises en œuvre (lecteurs d’écran, navigation assistée). Malgré cela, les principes fondamentaux des référentiels RGAA et WCAG ont été appliqués dans l’ensemble de l’interface.
 
3.5. Écoconception (optimisations front/back, performances)
Dans le cadre du développement d’IziLife, j’ai intégré une démarche d’écoconception visant à limiter l’empreinte environnementale du site, sans compromettre l’accessibilité ni la performance.
Actions mises en place
●	Réduction du poids des pages en limitant les dépendances externes et les scripts inutiles

●	Utilisation du format WebP pour les images, avec compression automatique côté serveur

●	Lazy loading des images pour éviter les chargements inutiles

●	Mise en cache efficace côté client grâce à TanStack Query

●	Pages épurées, sans animations superflues ni composants visuels lourds

●	Front-end compilé avec Vite, pour un build optimisé et rapide à charger

Résultat mesuré
Un audit réalisé via l’outil Ecograder donne un score de 71 sur 100, avec une empreinte estimée à 0.11 g de CO₂ par chargement de page. Le poids total moyen est de 289 Ko, soit 153 % plus léger que la moyenne des sites analysés.
L’impact carbone est bien maîtrisé sur les scripts, images et ressources statiques. Le principal point à améliorer reste l’hébergement, qui n’est pas alimenté par de l’énergie renouvelable.
Limite actuelle
Le serveur est hébergé sur un VPS Vultr classique, qui n’est pas certifié green hosting. Ce choix a été motivé par des contraintes budgétaires, mais pourrait être réévalué dans le futur pour renforcer la cohérence environnementale du projet.
Le rapport Ecograder est joint en annexe (cf. p. 72).
 
3.6. Tests & validation
Les tests ont été réalisés à la fois manuellement et automatiquement tout au long du développement du projet IziLife, afin d'assurer la fiabilité des fonctionnalités essentielles et d’identifier les éventuelles régressions.
Tests manuels
●	Vérification systématique de chaque fonctionnalité en local et en production

●	Contrôle du fonctionnement des formulaires, filtres, interactions (likes, favoris, commentaires)

●	Tests spécifiques sur les rôles utilisateurs : visiteur, utilisateur connecté, administrateur

●	Navigation complète au clavier (accessibilité)

●	Scénarios simulés d’erreur : mauvais format d’image, tentative de publication sans email validé, données manquantes
Tests automatisés
Des tests end-to-end ont été mis en place avec Cypress, notamment pour couvrir le scénario d'inscription utilisateur :
●	Saisie du formulaire avec des données valides

●	Validation des messages d’erreur en cas d’invalidité

●	Envoi de la demande et retour visuel de confirmation
Le test couvre l’enchaînement complet du parcours sans intervention manuelle (cf. p. 73).
Limites
Par manque de temps, je n’ai pas pu développer autant de tests automatisés que prévu. L’authentification, les cas d’erreur API, ou encore les publications sont testées manuellement à ce stade.
L’ajout de tests automatisés (unitaires, intégration API, E2E plus complets) fait partie des axes d’amélioration prévus à court terme.
 
4. Déploiement et CI/CD
Le déploiement d’IziLife a été conçu pour être automatisé, conteneurisé et supervisé, tout en restant simple et économique. Il repose sur Docker, GitLab CI/CD, un VPS Vultr, Nginx, et des outils de monitoring.
 
4.1. Conteneurisation avec Docker
L’ensemble des services IziLife est conteneurisé avec Docker pour garantir un déploiement fiable, reproductible et isolé.
Services conteneurisés
La stack comprend plusieurs services, orchestrés avec Docker Compose :
●	Le front-end React (buildé puis servi via Nginx)

●	Le back-end NestJS (compilé et exécuté en mode production)

●	La base de données PostgreSQL

●	Le stockage objet MinIO pour les images

●	Adminer (outil de visualisation de la base)

●	Portainer (interface de gestion Docker)

Seuls le front et le back disposent de Dockerfiles dédiés, les autres services utilisent les images officielles.
Réseau interne
Tous les conteneurs communiquent dans un réseau Docker privé. Seul Nginx est exposé publiquement pour servir l’application, rediriger les requêtes vers l’API et sécuriser les accès.


Structure du projet sur le serveur
Le projet est hébergé sur un VPS Debian chez Vultr. Les fichiers sont organisés dans un répertoire /sites/izilife contenant :
●	le fichier .env.prod avec les variables d’environnement (cf. p. 74)

●	le fichier docker-compose.yml de production (cf. p. 68)

●	le dossier backups/ contenant les dumps de la base PostgreSQL

Les volumes sont montés pour assurer la persistance des données, même après un redéploiement ou un redémarrage du serveur.
 
4.2. Pipeline GitLab CI/CD
Le déploiement de l’application est automatisé via une pipeline GitLab CI/CD. Celle-ci gère la construction des images Docker, leur publication, la sauvegarde de la base PostgreSQL et la mise à jour du serveur distant (cf. p. 69-70).
Étapes du pipeline
1.	Build des images

○	Le front et le back sont buildés dans deux jobs séparés

○	Les images sont taguées avec front:latest et back:latest

○	Elles sont poussées dans le GitLab Container Registry

2.	Sauvegarde de la base PostgreSQL

○	Un dump compressé est généré via pg_dump dans le conteneur de la base

○	Le fichier est stocké dans le répertoire backups/ sur le serveur

○	Les sauvegardes de plus de 7 jours sont automatiquement supprimées

3.	Déploiement distant

○	Le serveur est contacté via SSH avec une clé sécurisée

○	Les images sont récupérées avec docker pull

○	Les services front et back sont redéployés avec docker service update --force

Variables et sécurité
●	Les identifiants Docker, clés SSH et hosts autorisés sont stockés en tant que variables CI GitLab

●	Aucun secret n’est présent en clair dans le dépôt

Avantages de cette configuration
●	Déploiement automatique à chaque push sur la branche main

●	Aucune action manuelle requise pour mettre à jour la production

●	Traçabilité des déploiements depuis l’interface GitLab
 
4.3. Hébergement sur serveur Vultr
L’application IziLife est déployée sur un serveur VPS fourni par Vultr. Ce choix m’a permis de garder un contrôle total sur l’environnement tout en respectant les contraintes budgétaires.
Caractéristiques du serveur
●	Fournisseur : Vultr
●	Localisation : Paris
●	Système : Debian 12 x64
●	Ressources : 1 vCPU, 1 Go de RAM, 32 Go de stockage NVMe
●	Budget mensuel : environ 4 €

Le serveur héberge l’ensemble de la stack Docker (frontend, backend, base de données, stockage, outils de supervision), accessible uniquement via SSH.
Choix de l’hébergement
Le VPS Vultr m’a offert une grande flexibilité à moindre coût. Ce choix m’a permis d’installer manuellement tous les outils nécessaires (Docker, Nginx, Certbot, Portainer) et de tester l’ensemble du cycle de déploiement sans passer par un PaaS.
La seule limite identifiée est l’absence de label green hosting, qui impacte légèrement le score d’écoconception. Cette contrainte pourrait être levée dans le futur via une migration vers un hébergeur plus écologique.
 
4.4. Supervision et maintenance (Portainer, logs, backups)
Une supervision légère mais suffisante a été mise en place pour assurer le bon fonctionnement de l’application en production et intervenir rapidement en cas d’anomalie.
Supervision avec Portainer
L’interface Portainer installée sur le serveur permet de :
●	visualiser l’état des conteneurs (actif, arrêté, redémarré)
●	consulter les logs en temps réel
●	relancer ou mettre à jour un service
●	gérer les volumes, réseaux et configurations Docker
Cette interface facilite les interventions sans avoir à passer uniquement par la ligne de commande.
Logs applicatifs
Les logs de l’application sont consultables à plusieurs niveaux :
●	via les services Docker (docker compose logs)
●	via l’interface Portainer
●	via les fichiers Nginx (access.log et error.log)
Ces outils permettent de détecter rapidement les erreurs HTTP, les échecs de démarrage d’un service ou les erreurs internes de l’API.
Sauvegarde automatisée de la base
Un job dans la pipeline GitLab CI effectue une sauvegarde complète de la base PostgreSQL à chaque push sur main :
●	dump compressé généré depuis le conteneur PostgreSQL
●	enregistrement dans /sites/izilife/backups/YYYY-MM-DD
●	suppression automatique des sauvegardes de plus de 7 jours
Cette solution simple et fiable permet une restauration rapide en cas de besoin. 
4.5. Sécurité et conformité en production
La sécurité a été prise en compte à tous les niveaux, du serveur à l’application, pour garantir la confidentialité des données, la fiabilité des services et la conformité aux bonnes pratiques du web.
Accès au serveur
●	L’accès SSH est limité à une authentification par clé privée uniquement.

●	Aucun port inutile n’est ouvert. Seul Nginx accepte les connexions entrantes via HTTPS.

●	Le serveur n’héberge qu’un seul projet, ce qui limite les risques liés à la mutualisation.
Réseau et exposition
●	Tous les services (API, base, stockage) communiquent via un réseau Docker interne non exposé.

●	Seul Nginx est exposé au public, jouant le rôle de reverse proxy pour router les requêtes vers les bons services.

●	MinIO et Adminer sont accessibles uniquement via des routes sécurisées.
Sécurisation des données et fichiers
●	Les mots de passe sont hashés avec bcrypt avant stockage.

●	Les fichiers envoyés par les utilisateurs sont vérifiés, renommés, compressés et stockés de façon sécurisée dans MinIO.

●	L’envoi de mails (confirmation, réinitialisation) est effectué via SMTP sécurisé.

HTTPS et certificats
●	Un certificat SSL est généré avec Let’s Encrypt à l’aide de Certbot.

●	Toutes les requêtes HTTP sont redirigées vers HTTPS.

●	Le renouvellement du certificat est automatique.
Variables sensibles et configuration
●	Les clés d’accès, tokens et identifiants sont centralisés dans un fichier .env.prod non versionné.

●	En CI/CD, les variables sont injectées depuis GitLab CI Variables, sans apparaître dans le dépôt.

●	L’environnement de production ne conserve aucun log contenant des données personnelles.
Cette configuration assure un cadre sécurisé et conforme aux attentes d’un projet web en production.
 
 
5. Bilan et améliorations futures
 
5.1. Bilan personnel et professionnel
Ce projet m’a permis de mettre en œuvre de manière concrète l’ensemble des compétences acquises durant ma formation CDA, tout en donnant du sens à mon travail par la portée inclusive d’IziLife.
Sur le plan technique, j’ai pu concevoir, développer, sécuriser et déployer une application complète, en autonomie. Cela m’a demandé de jongler entre les responsabilités de développeur frontend, backend, architecte de base de données, intégrateur DevOps et gestionnaire de projet. Cette expérience a renforcé ma rigueur, ma capacité d’organisation et mon autonomie technique.
Sur le plan humain, ce projet m’a permis de porter un sujet qui me tient à cœur. En tant que personne en situation de handicap, j’ai voulu créer un outil utile, concret, tourné vers le partage et l’entraide. C’est aussi un projet que j’aimerais continuer à faire évoluer au-delà de l’examen.
Ce travail m’a confirmé que je souhaite m’orienter vers des projets où mes compétences techniques peuvent avoir un impact positif réel sur la vie des utilisateurs.
 
5.2. Compétences mobilisées
Le projet IziLife m’a permis de mobiliser l’ensemble des compétences attendues dans le cadre du titre de Concepteur Développeur d’Applications, en particulier dans les domaines suivants :
Conception et modélisation
●	Analyse des besoins utilisateurs et rédaction de User Stories

●	Modélisation de la base de données (MCD, MLD, MPD) avec Prisma

●	Élaboration de diagrammes UML (cas d’utilisation, séquence)

●	Conception d’interface avec Figma, en tenant compte des contraintes d’accessibilité
Développement front-end et back-end
●	Création d’une interface en React avec Vite et TypeScript

●	Développement d’une API REST sécurisée avec NestJS

●	Intégration des formulaires avec validation via Zod

●	Mise en place de l’authentification, de la gestion des rôles et des permissions

●	Connexion à une base PostgreSQL via Prisma ORM
Sécurité et accessibilité
●	Hashage des mots de passe, validation serveur, JWT

●	Respect des bonnes pratiques RGPD

●	Application des recommandations WCAG dans l’interface
Tests, qualité et performance
●	Tests manuels des parcours critiques

●	Mise en place de tests E2E avec Cypress

●	Optimisation des images et des performances (score Lighthouse)
DevOps et déploiement
●	Conteneurisation avec Docker et Docker Compose et supervision avec Portainer

●	Mise en production sur un VPS avec Nginx

●	Pipeline GitLab CI/CD avec déploiement automatique et sauvegarde de base de données
Gestion de projet
●	Organisation en sprints agiles

●	Suivi des tâches via Trello

●	Documentation complète tout au long du développement
Ce projet m’a permis de mettre en pratique tous les aspects du métier, du recueil du besoin jusqu’au déploiement, dans un contexte concret et porteur de sens.
 
5.3. Fonctionnalités et extensions prévues
Plusieurs fonctionnalités complémentaires sont envisagées pour faire évoluer IziLife après la version initiale. Elles ont été identifiées à partir de retours utilisateurs ou comme évolutions naturelles de l’architecture existante.
Recommandations intelligentes
Ajouter une logique de recommandation de solutions ou de discussions, en fonction des catégories consultées, des likes, ou du profil utilisateur. Cela permettrait de personnaliser l’expérience et d’encourager la découverte de contenus utiles.
Carte interactive
Intégrer une carte pour visualiser les solutions de type lieu. Cela offrirait une interface géographique intuitive, avec filtres par accessibilité ou par type de lieu.
Mode admin amélioré
Étendre les fonctionnalités du tableau de bord administrateur : tri, recherche, statistiques, filtrage avancé des signalements, historique de modération.
Espace utilisateur enrichi
Ajouter une page profil plus complète avec historique des publications, statistiques personnelles, badges communautaires, ou encore suggestions de contenus basées sur l’activité.
Ces fonctionnalités sont conçues pour rester cohérentes avec l’objectif du projet : proposer une plateforme accessible, simple d’utilisation, mais suffisamment évolutive pour accompagner des usages variés.
 
5.4. Pistes d’optimisation technique et UX
Même si l’application est fonctionnelle, plusieurs axes d’amélioration ont été identifiés pour renforcer la qualité technique, la fluidité d’utilisation et la maintenabilité à long terme.
Tests automatisés
Le projet ne dispose pour l’instant que d’un test E2E sur l’inscription. L’objectif est d’ajouter :
●	des tests unitaires sur les services back (NestJS + Jest)

●	des tests d’intégration pour les appels API

●	des scénarios E2E plus complets avec Cypress (publication, commentaire, signalement…)

Responsive et accessibilité avancée
L’interface est globalement responsive et accessible, mais peut être améliorée sur certains points :
●	meilleure gestion de l’ordre de tabulation

●	mise en conformité renforcée avec ARIA

●	compatibilité renforcée avec les lecteurs d’écran
Refonte du modèle de données
Actuellement, les solutions et discussions partagent le même système d’interaction (like, favoris, commentaires) via un champ target_type. Une amélioration envisagée serait de supprimer ce polymorphisme au profit de relations directes, plus claires, avec des clés étrangères explicites.
Upload intelligent
L’ajout d’un assistant automatisé pour détecter ou remplir certains champs (comme le titre ou l’image principale à partir d’une URL) permettrait d’alléger la saisie côté utilisateur et d’augmenter la qualité des données.
Ces optimisations visent à renforcer la robustesse de l’application et à faciliter son évolution à moyen terme.
 
 
5.5. Perspectives post-certification
Au-delà de l’examen, IziLife est un projet que je souhaite faire vivre. Il repose sur un besoin réel, identifié à partir de mon expérience personnelle, et pourrait à terme bénéficier à une communauté plus large.
Plusieurs pistes sont envisagées à court et moyen terme :
●	Continuer à enrichir la plateforme, notamment en développant les fonctionnalités prévues et en améliorant l’expérience utilisateur
●	Recueillir des retours concrets d’utilisateurs en situation de handicap, d’aidants ou de professionnels pour ajuster l’outil à leurs usages réels
●	Échanger avec des associations, collectivités ou structures médico-sociales qui pourraient intégrer IziLife dans leur réseau ou recommander la plateforme
●	Étudier la possibilité d’ouvrir le projet à d’autres contributeurs ou à une communauté open source
●	Approfondir les aspects sécurité, accessibilité et performance pour en faire un projet de référence dans le domaine de l’inclusion numérique

Sur le plan personnel, cette expérience a renforcé mon envie de m’investir dans des projets utiles, concrets, techniquement exigeants mais porteurs de sens. Je souhaite continuer à évoluer dans des environnements où la technique est au service de l’humain.
 
 
6. Annexes
Les annexes suivantes permettent de compléter et d’illustrer les éléments développés dans le dossier.
MCD :
 


MLD :
Diagrammes de cas d’utilisation :
User Stories : 
US01 - Inscription utilisateur :
En tant qu'utilisateur, je veux m'inscrire sur la plateforme en renseignant un pseudonyme, une adresse email et un mot de passe afin d'accéder aux fonctionnalités réservées aux membres.
Critères d’acceptation :
●	L'utilisateur peut saisir un pseudo, une adresse mail valide, et un mot de passe sécurisé.
●	Le pseudo doit être unique.
●	L’adresse mail doit être unique et valide (format standard).
●	Le mot de passe doit respecter les critères de sécurité :
●	Minimum de 8 caractères.
●	Au moins une lettre majuscule.
●	Au moins une lettre minuscule.
●	Au moins un chiffre.
●	Au moins un caractère spécial.
●	Après l'inscription, l'utilisateur reçoit un mail pour confirmer son adresse email (lié à US04).
●	L'inscription échoue si les informations sont manquantes, incorrectes ou déjà utilisées (pseudo/email).
●	L'utilisateur inscrit sans validation de mail ne peut pas accéder aux fonctionnalités de publication de solutions, de discussions ou de commentaires tant que son mail n'est pas confirmé.
●	L’utilisateur est notifié clairement du succès ou des erreurs lors de l’inscription.
US02 - Connexion / Déconnexion utilisateur
En tant qu'utilisateur, je veux pouvoir me connecter à mon compte en renseignant mon adresse email et mon mot de passe, puis me déconnecter à tout moment, afin de gérer de façon sécurisée l'accès à mon compte et à mes informations personnelles.
Critères d’acceptation :
Connexion :
●	L’utilisateur peut saisir son email et son mot de passe pour se connecter.
●	Le formulaire vérifie que l’email existe et que le mot de passe est correct.
●	L'utilisateur reçoit une notification en cas d'erreur (identifiants incorrects, compte banni) et une notification de succès lors d'une connexion réussie.
Déconnexion :
●	L’utilisateur connecté peut se déconnecter facilement depuis son espace personnel.
●	Après déconnexion, l’utilisateur ne peut plus accéder aux fonctionnalités réservées aux membres.




US03 - Réinitialisation du mot de passe
En tant qu'utilisateur, je veux pouvoir réinitialiser mon mot de passe en cas d'oubli en renseignant mon adresse email, afin de récupérer l'accès à mon compte rapidement et de façon sécurisée.
Critères d’acceptation :
●	L'utilisateur peut demander une réinitialisation de mot de passe en indiquant l’adresse email associée à son compte.
●	Si l’adresse email renseignée existe, l'utilisateur reçoit un mail contenant un lien unique et temporaire de réinitialisation.
●	Le lien envoyé par email possède une durée de validité limitée (ex : 1 heure).
●	En suivant le lien, l'utilisateur accède à une page sécurisée lui permettant de définir un nouveau mot de passe.
●	Le nouveau mot de passe doit respecter les mêmes critères de sécurité que lors de l’inscription :
●	Minimum de 8 caractères
●	Au moins une lettre majuscule
●	Au moins une lettre minuscule
●	Au moins un chiffre
●	Au moins un caractère spécial
●	Après réinitialisation, l'utilisateur reçoit une notification confirmant que son mot de passe a été mis à jour avec succès.
●	L'utilisateur est informé clairement en cas d'erreur ou d'échec (email introuvable, lien expiré, problème technique…).
US04 - Confirmation de l’adresse mail
En tant qu'utilisateur nouvellement inscrit, je veux pouvoir confirmer mon adresse email en recevant un lien de confirmation afin de disposer d'un compte vérifié et d'accéder pleinement aux fonctionnalités de la plateforme.
Critères d’acceptation :
●	Après l'inscription, l'utilisateur reçoit automatiquement un email contenant un lien unique et sécurisé permettant la confirmation de son adresse email.
●	Le lien envoyé par email possède une durée de validité limitée (ex : 48 heures).
●	En suivant ce lien, l’utilisateur confirme immédiatement son email, ce qui active complètement son compte.
●	L’utilisateur reçoit une notification claire confirmant la réussite de l’opération.
●	Si le lien est expiré ou invalide, l'utilisateur est informé clairement et peut demander un nouvel envoi du lien de confirmation depuis son espace personnel.
●	Tant que l’adresse email n'est pas confirmée, l’utilisateur est limité dans ses interactions (impossibilité de publier des solutions, discussions ou commentaires).
US05 - Gestion du profil utilisateur
En tant qu'utilisateur connecté, je veux pouvoir modifier les informations de mon profil (pseudo, email, image de profil, mot de passe…) afin de maintenir mon profil personnel à jour et conforme à mes préférences.
Critères d’acceptation :
●	L'utilisateur peut modifier son pseudonyme (qui doit rester unique).
●	L'utilisateur peut modifier son adresse email. En cas de modification de l'email, il doit reconfirmer sa nouvelle adresse en cliquant sur un lien reçu par email.
●	L'utilisateur peut modifier son image de profil en téléchargeant une nouvelle image.
●	L'utilisateur peut modifier son mot de passe à condition de renseigner son ancien mot de passe ainsi que le nouveau, respectant les mêmes critères de sécurité qu'à l'inscription :
●	8 caractères minimum
●	Au moins une majuscule
●	Au moins une minuscule
●	Au moins un chiffre
●	Au moins un caractère spécial
●	Après chaque modification réussie, l'utilisateur reçoit une notification claire lui confirmant l'opération.
●	En cas d'erreur (pseudo ou email déjà utilisé, ancien mot de passe incorrect, format d'image invalide, etc.), l'utilisateur reçoit une notification claire l'informant précisément du problème.
●	Toutes les modifications (sauf l’email) sont immédiatement effectives après validation réussie. La modification de l’email est effective uniquement après confirmation de la nouvelle adresse.
US06 - Réception de notifications utilisateur
En tant qu'utilisateur connecté, je veux recevoir des notifications lors d’événements importants (réponses à mes discussions, commentaires sur mes solutions ou commentaires, activité de modération, etc.) afin d’être informé en temps réel des interactions sur la plateforme.
Critères d’acceptation :
●	L'utilisateur reçoit une notification lorsqu'un autre utilisateur commente l'une de ses solutions, discussions ou l'un de ses commentaires.
●	L'utilisateur reçoit une notification lorsqu'une de ses solutions ou discussions est validée ou rejetée par la modération.
●	L'utilisateur reçoit une notification lorsqu'un de ses signalements est traité par un administrateur.
●	Les notifications sont visibles dans un espace dédié facilement accessible depuis son compte utilisateur.
●	Chaque notification indique clairement le type d'événement, l'auteur de l'action et un lien direct vers le contenu concerné.
●	Les notifications possèdent un statut "non-lu" ou "lu", et l'utilisateur peut identifier facilement et marquer les notifications comme lues.
US07 - Publication d'une solution
En tant qu'utilisateur connecté, je veux publier une solution (objet, service ou lieu accessible) afin de partager des ressources utiles qui peuvent améliorer le quotidien des autres membres de la communauté.
Critères d’acceptation :
Formulaire de création :
●	L’utilisateur connecté peut accéder à un formulaire de création de solution.
●	Le formulaire doit contenir les champs suivants :
●	URL (optionnel)
●	Titre (obligatoire)
●	Description (obligatoire)
●	Type de solution (Objet / Service / Lieu) (obligatoire)
●	Prix (obligatoire)
●	Catégories (obligatoire, au minimum une sélectionnée)
●	Téléchargement d’images (obligatoire, maximum 8) avec la possibilité de définir une image principale.
Fonctionnement attendu :
●	L'utilisateur est notifié de la réussite ou de l’échec de la publication (messages clairs).
●	La solution nouvellement créée est enregistrée avec le statut "en attente de validation" (pending).
●	Tant que la solution n’a pas été validée par un administrateur (lié à l’US19), elle n’est pas visible par les autres utilisateurs.
●	Une fois la validation effectuée, la solution passe en statut published et devient visible par tous les utilisateurs de la plateforme.
US08 - Recherche de solutions
En tant qu'utilisateur, je veux pouvoir rechercher des solutions selon différents critères (catégories, type, prix, mots-clés) afin de trouver rapidement des ressources adaptées à mes besoins.
Critères d’acceptation :
Fonctionnalité de recherche :
●	L’utilisateur peut accéder à une page listant les solutions publiées.
●	L’utilisateur peut rechercher des solutions selon les critères suivants :
●	Catégories (filtres multiples possibles)
●	Type de solution (Objet / Service / Lieu)
●	Plage de prix (min / max)
●	Mots-clés (recherche par titre ou description)
Fonctionnement attendu :
●	Les solutions affichées respectent les filtres appliqués.
●	La recherche par mots-clés est insensible à la casse (majuscules/minuscules).
●	Les résultats sont triés par défaut par date de publication décroissante (les plus récentes en premier).
●	En cas de recherche sans résultat, un message clair informe l’utilisateur qu’aucune solution ne correspond à sa recherche.
US09 - Visualisation du détail d'une solution
En tant qu'utilisateur, je veux visualiser le détail d'une solution (images, description, prix, auteur) et ses commentaires afin d'obtenir toutes les informations nécessaires sur la ressource partagée.
Critères d’acceptation :
Affichage des informations de la solution :
●	L'utilisateur peut accéder à une page de détail pour chaque solution publiée.
●	Les informations suivantes doivent être affichées :
●	Titre
●	Description complète
●	Type de solution (Objet / Service / Lieu)
●	Prix
●	URL (optionnelle)
●	Catégories associées
●	Images de la solution (affichage d’une galerie avec image principale mise en avant)
●	Pseudo de l’auteur de la solution
●	Date de création
Fonctionnalité de commentaire :
●	Tous les utilisateurs peuvent voir les commentaires publiés sous la solution.
●	Les commentaires doivent afficher :
●	Le contenu du commentaire
●	Le pseudo de l’auteur
●	La date de publication
●	Si la solution n’a aucun commentaire, un message indique qu’il n’y en a pas encore.
Fonctionnalités complémentaires :
●	L’utilisateur connecté peut ajouter un commentaire (lié à l’US15).
●	L’utilisateur connecté peut indiquer qu’il aime la solution (lié à l’US14).
●	Un bouton permet de signaler la solution ou un commentaire (lié à l’US17).
US10 - Création d'une discussion
En tant qu'utilisateur connecté, je veux créer une discussion sur une thématique liée au handicap afin d'obtenir des conseils, des retours d'expérience ou de partager des informations utiles avec les autres membres.
Critères d’acceptation :
Formulaire de création :
●	L’utilisateur connecté peut accéder à un formulaire de création de discussion.
●	Le formulaire doit contenir les champs suivants :
●	Titre de la discussion (obligatoire)
●	Contenu de la discussion (obligatoire)
●	Catégorie de discussion (obligatoire, une seule catégorie sélectionnable)
●	Catégories de handicap concernées (optionnel, plusieurs catégories sélectionnables)
Fonctionnement attendu :
●	L'utilisateur est notifié de la réussite ou de l’échec de la création de la discussion (messages clairs).
●	La discussion nouvellement créée est enregistrée avec le statut "en attente de validation" (pending).
●	Tant que la discussion n’a pas été validée par un administrateur (lié à l’US19), elle n’est pas visible par les autres utilisateurs.
●	Une fois validée, la discussion passe en statut published et devient visible par tous les utilisateurs de la plateforme.
●	La discussion peut ensuite recevoir des commentaires d'autres utilisateurs (lié à l’US15).
US11 - Recherche de discussions
En tant qu'utilisateur, je veux pouvoir rechercher des discussions selon différents critères (catégorie de discussion, catégories de handicap, mots-clés) afin de trouver rapidement des échanges pertinents et adaptés à mes besoins.
Critères d’acceptation :
Fonctionnalité de recherche :
●	L’utilisateur peut accéder à une page listant les discussions publiées (statut published uniquement).
●	L’utilisateur peut rechercher des discussions selon les critères suivants :
●	Catégorie de discussion (obligatoire — filtre unique)
●	Catégories de handicap (optionnel — filtres multiples)
●	Mots-clés (recherche par titre et contenu de la discussion)
Fonctionnement attendu :
●	Les discussions affichées respectent les filtres appliqués.
●	La recherche par mots-clés est insensible à la casse.
●	Les résultats sont triés par défaut par date de création décroissante (les plus récentes en premier).
●	En cas de recherche sans résultat, un message indique clairement à l’utilisateur qu’aucune discussion ne correspond à ses critères.
US12 - Consultation d’une discussion et de ses commentaires
En tant qu'utilisateur, je veux consulter une discussion et les commentaires associés afin de bénéficier des échanges et des conseils partagés par la communauté.
Critères d’acceptation :
Affichage des informations de la discussion :
●	L’utilisateur peut accéder à une page de détail d’une discussion publiée (statut published uniquement).
●	Les informations suivantes doivent être affichées :
●	Titre de la discussion
●	Contenu complet de la discussion
●	Catégorie de discussion
●	Catégories de handicap concernées (s’il y en a)
●	Pseudo de l’auteur de la discussion
●	Date de création de la discussion
Affichage des commentaires associés :
●	Tous les utilisateurs peuvent consulter les commentaires publiés sous la discussion (statut published uniquement).
●	Chaque commentaire doit afficher :
●	Contenu du commentaire
●	Pseudo de l’auteur
●	Date de création
●	Si aucun commentaire n’a encore été publié, un message doit l’indiquer clairement.
Fonctionnalités complémentaires :
●	Un utilisateur connecté peut commenter la discussion (lié à l’US15).
●	Un utilisateur connecté peut indiquer qu’il aime la discussion ou un commentaire (lié à l’US14).
●	Un utilisateur connecté peut signaler un commentaire ou la discussion (lié à l’US17).
US13 - Ajouter une solution ou une discussion en favoris
En tant qu'utilisateur connecté, je veux ajouter une solution ou une discussion à mes favoris afin de les retrouver facilement et rapidement depuis mon espace personnel.
Critères d’acceptation :
Fonctionnalité d’ajout aux favoris :
●	L’utilisateur connecté peut ajouter une solution ou une discussion à ses favoris en cliquant sur un bouton spécifique (ex : icône étoile).
●	Si l’élément est déjà en favoris, un second clic permet de le retirer des favoris.
●	Un message clair confirme à l’utilisateur l’ajout ou la suppression d’un élément des favoris.
Fonctionnalité de consultation des favoris :
●	L’utilisateur connecté dispose d’un espace dédié (page personnelle) listant toutes ses solutions et discussions ajoutées en favoris.
US14 - J’aime une solution, une discussion ou un commentaire
En tant qu'utilisateur connecté, je veux pouvoir indiquer que j’aime une solution, une discussion ou un commentaire afin d’encourager et valoriser les contributions des autres membres de la communauté.
 
Critères d’acceptation :
Fonctionnalité d’ajout d’un "like" :
●	L’utilisateur connecté peut cliquer sur un bouton spécifique (ex : icône cœur) pour aimer :
●	Une solution
●	Une discussion
●	Un commentaire
●	Si l’utilisateur a déjà aimé un élément, un second clic permet de retirer son "like".
●	Un compteur de likes est affiché à côté de chaque élément (nombre de personnes ayant aimé).
Fonctionnement attendu :
●	L’utilisateur reçoit un retour visuel immédiat lors de l’ajout ou suppression de son like.
●	Les utilisateurs non connectés ne peuvent pas aimer un élément.
●	Chaque utilisateur ne peut aimer un élément qu’une seule fois à la fois.
US15 - Commenter une solution ou une discussion (ou répondre à un commentaire)
En tant qu'utilisateur connecté, je veux commenter une solution ou une discussion afin de donner mon avis, poser une question ou partager mon expérience.
Je veux également pouvoir répondre à un commentaire existant afin de participer à un échange.
Critères d’acceptation :
Fonctionnalité de commentaire :
●	L'utilisateur connecté peut publier un commentaire :
●	Sur une solution
●	Sur une discussion
●	Le commentaire doit contenir un champ texte obligatoire.
●	L’utilisateur peut répondre à un commentaire existant (réponse directe, 5 niveaux d’arborescence).
Fonctionnement attendu :
●	Les commentaires sont publiés immédiatement après validation du formulaire (pas de modération préalable).
●	Les commentaires sont triés par date de création croissante (les plus anciens en premier).
●	Les réponses à un commentaire sont affichées directement sous le commentaire concerné.
●	L’utilisateur est notifié de la réussite ou de l’échec de la publication de son commentaire.
●	Tous les commentaires (commentaires principaux ou réponses) peuvent être signalés par un utilisateur connecté (lié à l’US17).

US16 - Modification et suppression de ses propres contenus
En tant qu'utilisateur connecté, je veux pouvoir modifier ou supprimer un contenu que j’ai moi-même publié (solution, discussion, commentaire) afin de corriger une erreur, mettre à jour une information ou supprimer un contenu devenu obsolète.
Critères d’acceptation :
Modification :
●	L’utilisateur connecté peut modifier uniquement ses propres contenus :
●	Solutions
●	Discussions
●	Commentaires
●	Pour les solutions et discussions :
●	Les mêmes règles de validation que lors de la création s’appliquent.
●	Après modification, le contenu repasse en statut pending et doit être validé par un administrateur avant d’être à nouveau publié.
●	Pour les commentaires :
●	L’utilisateur peut modifier son commentaire sans validation préalable.
●	La modification met à jour le champ updated_at.
Suppression :
●	L’utilisateur connecté peut supprimer uniquement ses propres contenus :
●	Solutions
●	Discussions
●	Commentaires
●	Suppression d’une solution ou d’une discussion :
●	Suppression définitive en base de données.
●	Suppression des images associées (solution).
●	Suppression des commentaires enfants.
●	Suppression des likes et favoris associés.
●	Suppression d’un commentaire :
●	Le commentaire n’est pas supprimé physiquement.
●	Le statut du commentaire passe à disabled.
●	Le contenu du commentaire est remplacé par la mention : "Commentaire désactivé".
●	Les réponses éventuelles au commentaire restent visibles.
US17 - Gestion des catégories (par un administrateur)
En tant qu’administrateur, je veux gérer les catégories de la plateforme (créer, modifier, supprimer) afin de structurer efficacement les contenus et faciliter la navigation des utilisateurs.
Critères d’acceptation :
Fonctionnalité de création d’une catégorie :
●	L’administrateur peut créer une nouvelle catégorie en renseignant :
●	Le nom de la catégorie (obligatoire)
●	Le type de la catégorie (obligatoire) :  handicap ou discussion
Fonctionnalité de modification d’une catégorie :
●	L’administrateur peut modifier le nom d’une catégorie existante.
Fonctionnalité de suppression d’une catégorie :
●	L’administrateur peut supprimer une catégorie uniquement si elle n’est pas utilisée dans un contenu (solution ou discussion).
●	Si la catégorie est utilisée, un message d’erreur informe l’administrateur que la suppression est impossible.
US18 - Signalement d’un contenu (solution, discussion ou commentaire)
En tant qu'utilisateur connecté, je veux pouvoir signaler un contenu inapproprié (solution, discussion ou commentaire) afin d’aider les administrateurs à maintenir un espace respectueux et sécurisé pour la communauté.
Critères d’acceptation :
Fonctionnalité de signalement :
●	L’utilisateur connecté peut signaler :
●	Une solution
●	Une discussion
●	Un commentaire
●	Lors du signalement, l’utilisateur doit obligatoirement sélectionner un motif parmi une liste prédéfinie (contenu inapproprié, insultant, spam, harcèlement, autre).
●	L’utilisateur peut ajouter un commentaire facultatif pour préciser les raisons du signalement.
Fonctionnement attendu :
●	Un utilisateur ne peut signaler le même contenu qu’une seule fois.
●	Une notification de confirmation informe l’utilisateur que son signalement a été pris en compte.
●	Tous les signalements sont accessibles aux administrateurs dans un espace dédié à la modération (lié à l’US19).
●	Les signalements n’ont aucun effet automatique (aucune suppression automatique) — ils doivent être traités manuellement par un administrateur.
US19 - Modération des contenus signalés (par un administrateur)
En tant qu’administrateur, je veux pouvoir consulter les signalements effectués par les utilisateurs sur les contenus (solutions, discussions, commentaires) afin de prendre les mesures adaptées et assurer le respect des règles de la plateforme.
Critères d’acceptation :
Consultation des signalements :
●	L’administrateur peut accéder à une liste des signalements effectués par les utilisateurs.
●	Pour chaque signalement, les informations suivantes sont affichées :
●	Type de contenu signalé (Solution, Discussion, Commentaire)
●	Motif du signalement (ReportReason)
●	Description facultative du signalement
●	Utilisateur ayant signalé
●	Date du signalement
●	Statut de traitement (ModerationActionType)
Actions de modération possibles :
●	L’administrateur peut appliquer une action de modération (ModerationActionType) :
●	approve : Valider le contenu sans action.
●	hide : Masquer temporairement le contenu (status disabled).
●	delete : Supprimer définitivement le contenu.
●	Aucune action automatique n’est appliquée lors du signalement.
●	L’administrateur peut ajouter un commentaire facultatif pour justifier l'action prise.
Fonctionnement attendu :
●	Après action de modération, l'utilisateur ayant signalé reçoit une notification l’informant que son signalement a été traité (lié à US06).
●	Les actions de modération sont tracées et stockées dans la table ContentModeration.
US20 - Gestion des comptes utilisateurs (par un administrateur)
En tant qu’administrateur, je veux pouvoir bannir ou activer un compte utilisateur afin d’empêcher les utilisateurs malveillants de nuire à la communauté et de garantir un espace respectueux et sécurisé.
Critères d’acceptation :
Consultation des utilisateurs :
●	L’administrateur peut accéder à la liste des utilisateurs inscrits sur la plateforme.
●	Les informations suivantes doivent être affichées :
●	Pseudo
●	Email
●	Statut du compte (Status) :
●	active (Actif)
●	pending (En attente de confirmation d’email)
●	banned (Banni)
●	Date d’inscription
Fonctionnalités disponibles :
●	L’administrateur peut bannir un utilisateur actif (active → banned).
●	L’administrateur peut réactiver un utilisateur banni (banned → active).
●	Après un bannissement :
●	L’utilisateur ne peut plus se connecter.
●	Un message spécifique doit lui indiquer que son compte est banni s’il tente de se connecter.
●	Après réactivation, l’utilisateur retrouve l’accès normal à son compte.


Sprints :
Sprint 1 — Maquettage UX/UI
Aucune User Story → travail uniquement sur Figma & retours utilisateurs.
Sprint 2 — Environnement Technique & Authentification
US	Fonctionnalité
US01	Inscription utilisateur
US02	Connexion / Déconnexion utilisateur
US03	Réinitialisation du mot de passe
US04	Confirmation de l’adresse mail
US05	Gestion du profil utilisateur

Sprint 3 — Gestion des Contenus (Publication)
US	Fonctionnalité
US07	Publication d'une solution
US10	Création d'une discussion

Sprint 4 — Consultation & Filtrage (MVP)
US	Fonctionnalité
US08	Recherche de solutions
US09	Visualisation du détail d'une solution
US11	Recherche de discussions
US12	Consultation du détail d'une discussion

Sprint 5 — Fonctionnalités Communautaires & Signalement
US	Fonctionnalité
US13	Ajouter solution ou discussion en favoris
US14	J’aime une solution, une discussion ou un commentaire
US15	Commenter une solution ou une discussion (ou répondre à un commentaire)
US16	Modification et suppression de ses propres contenus
US18	Signalement d’un contenu (solution, discussion ou commentaire)

Sprint 6 — Tableau de bord Administrateur + Notifications
US	Fonctionnalité
US17	Gestion des catégories (par un administrateur)
US19	Modération des contenus signalés (par un administrateur)
US20	Gestion des comptes utilisateurs (par un administrateur)
US06	Réception de notifications utilisateur
Sprint 7 — Tests, Sécurité & Accessibilité
Tests fonctionnels, sécurité, audit code, accessibilité WCAG.

Sprint 8 — Déploiement Docker & CI/CD
Containerisation, pipeline GitLab CI/CD, déploiement sur Vultr.

Sprint 9 — Finalisation, Documentation & Optimisations
Corrections finales, documentation complète, optimisations techniques.

Sprint 10 — Améliorations Continues
Roadmap post-projet, suivi KPIs, feedbacks utilisateurs.

Diagramme de séquence ( processus d’inscription ) :
Diagramme de séquence ( processus de connexion ) :
Diagramme de séquence ( réinitialisation du mot de passe ) :
Diagramme de séquence ( publication d’une solution ) :
Liste de solutions et détail d’une solution ( desktop ) :

Modale de connexion et d’inscription ( desktop ) :
Maquettes mobiles :
Dockerfile front :
Dockerfile back :
Docker-compose.yml (version de production) :
Fichier complet .gitlab-ci.yml


Configuration Nginx (extrait) :
 
 
Score Ecograder (empreinte carbone)
Capture du test Cypress (inscription utilisateur)
Exemple anonymisé du fichier .env.prod



