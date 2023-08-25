
# FolderTree Project
 
Ce projet consiste en un programme Python qui automatise la création d'une arborescence de dossiers pour un projet, l'initialisation d'un dépôt Git local, la création d'un dépôt distant sur GitHub, et l'ajout, le commit et le push de modifications vers le dépôt distant.

## Structure du Projet


├── data               #  repertoire contenant des données (brutes, propres)
│   ├── cleaned
│   └── raw
├── docs               #  repertoire contenant toute documentation utile
├── LICENSE
├── Makefile           #  fichier permettant d'automatiser des taches
├── models             #  repertoire contenant tous les modèles construits
├── notebooks          #  repertoire contenant tous les notebooks rédigés
│   └── main.ipynb
├── README.md
├── reports            #  repertoire contenant tous les rapports générés
├── requirements.txt   #  fichier contenant la liste des dépendances du projets
└── src                #  repertoire contenant tout code python utile
    └── utils.py

## Fonctionnalités

- Crée un fichier dans le répertoire du dépôt.
- Ajoute le fichier à la zone de suivi Git.
- Effectue un commit avec un message personnalisé.
- Pousse les modifications vers le dépôt distant.

## Configuration

1. Assurez-vous que vous avez installé Git sur votre système.
2. Clonez le dépôt GitHub sur votre machine locale : `git clone <URL_du_dépôt>`.
3. Modifiez la variable `root_directory` dans le programme pour pointer vers le chemin absolu de votre dépôt cloné.

## Utilisation

1. Exécutez le programme : `python script1.py`.
2. Saisissez le chemin absolu du dépôt cloné.
3. Le programme créera les fichiers et dossiers
4. Le fichier ou dossier sera ajouté, commité et poussé vers le dépôt distant.

## Avertissement

L'exécution de commandes Git via des scripts nécessite une compréhension approfondie de Git. Assurez-vous de comprendre les implications et testez sur un dépôt factice avant d'appliquer ce script à un projet réel.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez soumettre des problèmes ou des demandes d'extraction sur GitHub.

## Licence

Ce projet est sous licence MIT.

## Auteur

Créé par Lauriane MBAGDJE DORENAN
Contact : dmbagdjelauriane@gmail.com

## Remerciements

Ce projet a été inspiré par l'idée d'automatiser les tâches Git pour les projets.
