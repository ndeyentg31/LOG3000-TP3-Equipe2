
"""Tests unitaires des opérations de la calculatrice."""

from operators import add, subtract, multiply, divide


def test_add():
    """Vérifie que l'addition retourne la somme attendue."""
    assert add(5, 3) == 8


def test_subtract():
    """Vérifie que la soustraction respecte l'ordre des opérandes."""
    assert subtract(5, 3) == 2


def test_multiply():
    """Vérifie que la multiplication retourne le produit attendu."""
    assert multiply(5, 3) == 15


def test_divide():
    """Vérifie que la division conserve les décimales."""
    assert divide(5, 2) == 2.5
