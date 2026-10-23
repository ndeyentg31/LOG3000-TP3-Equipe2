# LOG3000 – TP3 : Calculatrice Web

## Équipe 2

## Objectif du projet

Ce projet consiste à améliorer une application web de calculatrice développée avec Python et Flask. Le travail vise à documenter le code existant, à identifier et corriger les bogues à l'aide de tests, et à utiliser GitHub pour faciliter la collaboration et la gestion des versions.

L'application permet d'effectuer quatre opérations arithmétiques : l'addition, la soustraction, la multiplication et la division.

Le projet comprend une interface HTML/CSS, des fonctions JavaScript pour la saisie des expressions et un serveur Flask pour effectuer les calculs.

## Prérequis

- Python 3
- pip
- Flask
- Git
- pytest (pour les tests)

## Installation

1. Cloner le dépôt :
   `git clone https://github.com/ndeyentg31/LOG3000-TP3-Equipe2.git`
2. Accéder au dossier du projet :
   `cd LOG3000-TP3-Equipe2`
3. Installer Flask :
   `python -m pip install flask`
4. Démarrer l'application :
   `python app.py`
5. Ouvrir un navigateur et accéder à :
   `http://127.0.0.1:5000/`

## Utilisation

1. Ouvrir l'application dans un navigateur.
2. Cliquer sur les boutons numériques pour saisir le premier nombre.
3. Sélectionner un opérateur (+, -, \* ou /).
4. Saisir le deuxième nombre.
5. Cliquer sur `=` pour afficher le résultat.
6. Cliquer sur `C` pour effacer l'expression.

## Tests

Les tests permettent de vérifier :

- Les quatre opérations arithmétiques.
- Les libellés des boutons 2, 8, * et /.

Installer les dépendances :

```bash
python -m pip install flask pytest
```

Exécuter les tests depuis la racine du projet :

```bash
python -m pytest tests/ -v
```

## Contribution

Pour contribuer au projet :

1. Créer une GitHub Issue pour signaler un bogue.
2. Décrire le problème, les étapes de reproduction et les résultats attendus.
3. Assigner l'Issue à un membre de l'équipe.
4. Créer une branche distincte pour chaque issue.
5. Effectuer les corrections sur la branche correspondante.
6. Exécuter les tests pour vérifier les corrections.
7. Ouvrir une Pull Request.
8. Faire réviser et fusionner la Pull Request dans `main`.

## Structure du projet

- `app.py` : serveur Flask et traitement des expressions.
- `operators.py` : fonctions des opérations arithmétiques.
- `templates/` : interface HTML et fonctions JavaScript.
- `static/` : styles CSS de la calculatrice.
- `tests/` : tests automatisés des opérations et de l'interface.

Chaque répertoire possède son propre fichier `README.md` décrivant son rôle, ses fichiers principaux et ses dépendances.
