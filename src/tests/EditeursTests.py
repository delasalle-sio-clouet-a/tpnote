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

def test_ajout_editeur_valide(database:Database):
    # résultat attendu : editeur ajouté
    assert False

def test_ajout_editeur_duplicata(database:Database):
    # résultat attendu : editeur NON ajouté
    assert False