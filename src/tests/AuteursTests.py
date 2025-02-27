import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_auteur_valide(database:Database):
    # résultat attendu : auteur ajouté
    assert False

def test_ajout_auteur_duplicata(database:Database):
    # résultat attendu : auteur NON ajouté
    assert False