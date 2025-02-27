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

def test_ajout_auteur_valide(database:Database):
    # résultat attendu : auteur ajouté
    auteur = Auteur(3, "Desbuts", "Jean-Marc")
    resultat = database.auteurs_insert(auteur)
    assert resultat == True

def test_ajout_auteur_duplicata(database:Database):
    # résultat attendu : auteur NON ajouté car l'id existe déjà
    auteur = Auteur(2, "Desbuts", "Jean-Marc")
    with pytest.raises(DuplicataException) as error:
        resultat = database.auteurs_insert(auteur)
    assert error.value == "Un auteur possède déjà cet identifiant."

def test_get_auteur_existant(database:Database):
    # résultat attendu : une instance d'Auteur est retournée
    auteur = database.auteurs_get_by_id("0")
    assert isinstance(auteur, Auteur)

def test_get_auteur_inexistant(database:Database):
    # résultat attendu : None est retourné
    auteur = database.auteurs_get_by_id("294974")
    assert auteur == None