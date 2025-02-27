import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_adherent_valide(db:Database):
    # résultat attendu : adhérent ajouté
    assert False

def test_ajout_adherent_duplicata(db:Database):
    # résultat attendu : adhérent NON ajouté
    assert False

def test_ajout_adherent_email_invalide(db:Database):
    # résultat attendu : adhérent NON ajouté
    assert False