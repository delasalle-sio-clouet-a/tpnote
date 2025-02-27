import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_editeur_valide(database:Database):
    # résultat attendu : editeur ajouté
    assert False

def test_ajout_editeur_duplicata(database:Database):
    # résultat attendu : editeur NON ajouté
    assert False