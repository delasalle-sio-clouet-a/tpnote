import pytest
from datetime import date, datetime

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

def test_ajout_adherent_valide(database:Database):
    # résultat attendu : adhérent ajouté
    adherent = Adherent("000474", "Ogne", "Paul", date(2002, 4, 29), False)
    resultat = database.adherents_insert(adherent)
    assert resultat == True

def test_ajout_adherent_duplicata(database:Database):
    # résultat attendu : adhérent NON ajouté car code_adherent déjà existant
    adherent = Adherent("000475", "Ogne", "Paul", date(2002, 4, 29), False)
    with pytest.raises(DuplicataException) as error:
        resultat = database.adherents_insert(adherent)
    assert str(error.value) == "Ce code adhérent est déjà utilisé."

def test_ajout_adherent_email_invalide(database:Database):
    # résultat attendu : adhérent NON ajouté car l'email n'est pas valide
    adherent = Adherent("000473", "Ogne", "Paul", date(2002, 4, 29), False)
    with pytest.raises(InvalidFormatException) as error:
        resultat = database.adherents_insert(adherent)
    assert str(error.value) == "Format de l'email invalide."

def test_ajout_adherent_code_longueur_invalide(database:Database):
    # résultat attendu : adhérent NON ajouté car le code adhérent n'est pas de 5 caractères
    adherent = Adherent("0004730", "Ogne", "Paul", date(2002, 4, 29), False)
    with pytest.raises(InvalidFormatException) as error:
        resultat = database.adherents_insert(adherent)
    assert str(error.value) == "Le code adhérent ne fait pas 5 caractères."

def test_ajout_adherent_code_caractere_invalide(database:Database):
    # résultat attendu : adhérent NON ajouté car le code adhérent ne contient pas que des chiffres
    adherent = Adherent("0O0473", "Ogne", "Paul", date(2002, 4, 29), False)
    with pytest.raises(InvalidFormatException) as error:
        resultat = database.adherents_insert(adherent)
    assert str(error.value) == "Le code adhérent contient des caractères non numériques."

def test_get_adherent_existant(database:Database):
    # résultat attendu : une instance d'Adherent est retournée
    adherent = database.adherents_get_by_code("000475")
    assert isinstance(adherent, Adherent)

def test_get_adherent_inexistant(database:Database):
    # résultat attendu : None est retourné
    adherent = database.adherents_get_by_code("000100")
    assert adherent == None