# Module templates

## Description

Ce répertoire contient le modèle HTML utilisé pour afficher l'interface de la calculatrice web.

## Fichiers principaux

- `index.html` : définit l'écran d'affichage, les boutons de la calculatrice et les fonctions JavaScript permettant de saisir ou d'effacer une expression.

## Dépendances et hypothèses

- Le fichier HTML est affiché par le serveur Flask à partir de `app.py`.
- Il utilise Jinja2 pour afficher le résultat du calcul transmis par le serveur.
- Il dépend du fichier `static/style.css` pour la mise en forme de l'interface.
- Les interactions avec les boutons nécessitent un navigateur prenant en charge JavaScript.
