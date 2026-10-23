
"""Tests des libellés des boutons de la calculatrice."""

from html.parser import HTMLParser

import pytest
from app import app


class ExtracteurBoutons(HTMLParser):
    """Extrait les libellés associés aux actions des boutons."""

    def __init__(self):
        """Initialise les libellés et l'état de lecture."""
        super().__init__()
        self.libelles = {}
        self.action = None
        self.texte = []

    def handle_starttag(self, tag, attrs):
        """Repère le début d'un bouton HTML."""
        if tag == "button":
            self.action = dict(attrs).get("onclick")
            self.texte = []

    def handle_data(self, data):
        """Récupère le texte visible du bouton courant."""
        if self.action is not None:
            self.texte.append(data)

    def handle_endtag(self, tag):
        """Enregistre le libellé à la fermeture du bouton."""
        if tag == "button" and self.action is not None:
            self.libelles[self.action] = "".join(self.texte).strip()
            self.action = None


@pytest.mark.parametrize("caractere", ["2", "8", "*", "/"])
def test_libelle_bouton(caractere):
    """Vérifie que le bouton affiche le caractère qu'il saisit."""
    with app.test_client() as client:
        reponse = client.get("/")

    assert reponse.status_code == 200

    extracteur = ExtracteurBoutons()
    extracteur.feed(reponse.get_data(as_text=True))

    action = f"appendToDisplay('{caractere}')"
    assert extracteur.libelles.get(action) == caractere
