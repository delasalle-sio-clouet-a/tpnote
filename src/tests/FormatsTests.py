import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_format_valide(database:Database):
    # résultat attendu : format ajouté
    assert False

def test_ajout_format_duplicata(database:Database):
    # résultat attendu : format NON ajouté
    assert False