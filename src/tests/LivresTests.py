import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_livre_valide(db:Database):
    # résultat attendu : livre ajouté
    assert False

def test_ajout_livre_isbn_invalide(db:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_isbn_valide_avec_tirets(db:Database):
    # résultat attendu : livre ajouté
    assert False

def test_ajout_livre_duplicata(db:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_format_invalide(db:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_auteur_invalide(db:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_editeur_invalide(db:Database):
    # résultat attendu : livre NON ajouté
    assert False