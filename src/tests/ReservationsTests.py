import pytest
from flask.testing import FlaskClient

def test_nouvelle_reservation_valide():
    # résultat attendu : reservation ajoutée
    assert False

def test_nouvelle_reservation_adherent_invalide():
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_livre_invalide():
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_date_debut_invalide():
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_adherent_maximum(): # créer une réservation lorsqu'un adhérent a le maximum de réservations en cours (>= 3)
    # résultat attendu : reservation NON ajoutée
    assert False

def test_fin_reservation_valide():
    # résultat attendu : reservation finalisée
    assert False

def test_fin_reservation_inexistante():
    # résultat attendu : reservation NON finalisée
    assert False

def test_fin_reservation_date_invalide():
    # résultat attendu : reservation NON finalisée
    assert False