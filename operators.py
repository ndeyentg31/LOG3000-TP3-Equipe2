"""Ce fichier contient les opérations arithmétiques de la calculatrice."""
def add(a,b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (int ou float): Premier nombre.
        b (int ou float): Deuxième nombre.

    Returns:
        int ou float: Résultat de a + b.
    """
    return a + b


def subtract(a, b):
    """
    Calcule la différence entre deux nombres.

    Args:
        a (int ou float): Nombre de départ.
        b (int ou float): Nombre à soustraire.

    Returns:
        int ou float: Résultat attendu de a - b.
    """
    return b - a

def multiply(a,b):
    """
    Calcule le produit de deux nombres.

    Args:
        a (int ou float): Premier facteur.
        b (int ou float): Deuxième facteur.

    Returns:
        int ou float: Résultat attendu de a * b.
    """
    return a ** b

def divide(a,b):
    """
    Calcule le quotient de deux nombres.

    Args:
        a (int ou float): Dividende.
        b (int ou float): Diviseur non nul.

    Returns:
        int ou float: Résultat attendu de a / b.
    """
    return a // b
