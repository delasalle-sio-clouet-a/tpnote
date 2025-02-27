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
    # résultat attendu : éditeur ajouté
    editeur = Editeur(2, "Ouest-France")
    resultat = database.editeurs_insert(editeur)
    assert resultat == True

def test_ajout_editeur_duplicata(database:Database):
    # résultat attendu : éditeur NON ajouté car l'id existe déjà
    editeur = Auteur(1, "Ouest-France")
    with pytest.raises(DuplicataException) as error:
        resultat = database.editeurs_insert(editeur)
    assert error.value == "Un éditeur possède déjà cet identifiant."

def test_get_editeur_existant(database:Database):
    # résultat attendu : une instance d'Editeur est retournée
    editeur = database.editeurs_get_by_id("0")
    assert isinstance(editeur, Editeur)

def test_get_editeur_inexistant(database:Database):
    # résultat attendu : None est retourné
    editeur = database.editeurs_get_by_id("294974")
    assert editeur == None