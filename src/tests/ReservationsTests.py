import pytest
from flask.testing import FlaskClient
from src.classes.CDatabase import Database

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

from src.exceptions.InvalidFormatException import InvalidFormatException
from src.exceptions.DuplicataException import DuplicataException

def test_nouvelle_reservation_valide(database:Database):
    # résultat attendu : reservation ajoutée
    assert False

def test_nouvelle_reservation_adherent_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_livre_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_date_debut_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée
    assert False

def test_nouvelle_reservation_adherent_maximum(database:Database): # créer une réservation lorsqu'un adhérent a le maximum de réservations en cours (>= 3)
    # résultat attendu : reservation NON ajoutée
    assert False

def test_fin_reservation_valide(database:Database):
    # résultat attendu : reservation finalisée
    assert False

def test_fin_reservation_inexistante(database:Database):
    # résultat attendu : reservation NON finalisée
    assert False

def test_fin_reservation_date_invalide(database:Database):
    # résultat attendu : reservation NON finalisée
    assert False