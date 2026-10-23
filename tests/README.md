
# Tests unitaires - Calculatrice LOG3000

## Objectif

Ce module contient les tests unitaires permettant de
vérifier le comportement des opérations arithmétiques
de la calculatrice.

## Dépendances

- Python 3
- Flask
- pytest

Installation :

```bash
python -m pip install pytest
```

## Exécution

Depuis la racine du projet :

```bash
python -m pytest tests/ -v
```

## Tests couverts

- test_add : vérifie l'addition.
- test_subtract : vérifie l'ordre des opérandes.
- test_multiply : vérifie la multiplication.
- test_divide : vérifie la division décimale.


### test_boutons.py

Ce fichier vérifie que les boutons de la calculatrice affichent les caractères correspondant à leurs actions :

- Bouton `2` : vérifie que le libellé affiché est `2`.
- Bouton `8` : vérifie que le libellé affiché est `8`.
- Bouton `*` : vérifie que le libellé affiché est `*`.
- Bouton `/` : vérifie que le libellé affiché est `/`.