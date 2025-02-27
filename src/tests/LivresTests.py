import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

def test_ajout_livre_valide(database:Database):
    # résultat attendu : livre ajouté
    assert False

def test_ajout_livre_isbn_invalide(database:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_isbn_valide_avec_tirets(database:Database):
    # résultat attendu : livre ajouté
    assert False

def test_ajout_livre_duplicata(database:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_format_invalide(database:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_auteur_invalide(database:Database):
    # résultat attendu : livre NON ajouté
    assert False

def test_ajout_livre_editeur_invalide(database:Database):
    # résultat attendu : livre NON ajouté
    assert False