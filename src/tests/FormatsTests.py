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

def test_ajout_format_valide(database:Database):
    # résultat attendu : éditeur ajouté
    format = Format(3, "Revue")
    resultat = database.formats_insert(format)
    assert resultat == True

def test_ajout_format_duplicata(database:Database):
    # résultat attendu : éditeur NON ajouté car l'id existe déjà
    format = Format(0, "Revue")
    with pytest.raises(DuplicataException) as error:
        resultat = database.formats_insert(format)
    assert str(error.value) == "Un éditeur possède déjà cet identifiant."

def test_get_format_existant(database:Database):
    # résultat attendu : une instance d'Editeur est retournée
    format = database.formats_get_by_id(0)
    assert isinstance(format, Format)

def test_get_format_inexistant(database:Database):
    # résultat attendu : None est retourné
    format = database.formats_get_by_id("15774")
    assert format == None