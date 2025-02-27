import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_auteur_valide(db:Database):
    # résultat attendu : auteur ajouté
    assert False

def test_ajout_auteur_duplicata(db:Database):
    # résultat attendu : auteur NON ajouté
    assert False