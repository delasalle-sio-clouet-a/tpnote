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
from src.exceptions.InvalidIsbnException import InvalidIsbnException
from src.exceptions.MissingDataException import MissingDataException

def test_ajout_livre_valide(database:Database):
    # résultat attendu : livre ajouté
    livre = Livre("0820000302", "Le jeu du trône", 0, 0, 0)
    resultat = database.livres_insert(livre)
    assert resultat == True

def test_ajout_livre_isbn_valide_avec_tirets(database:Database):
    # résultat attendu : livre ajouté
    livre = Livre("0-8200-0030-2", "Le jeu du trône", 0, 0, 0)
    resultat = database.livres_insert(livre)
    assert resultat == True

def test_ajout_livre_isbn_X_valide(database:Database):
    # résultat attendu : livre ajouté
    livre = Livre("123456789X", "Le jeu du trône", 0, 0, 0)
    resultat = database.livres_insert(livre)
    assert resultat == True

def test_ajout_livre_isbn_clef_invalide(database:Database):
    # résultat attendu : livre NON ajouté car clé de l'isbn est incorrecte
    livre = Livre("0820000300", "Le jeu du trône", 0, 0, 0)
    with pytest.raises(InvalidIsbnException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "La clé du code isbn est incorrecte."

def test_ajout_livre_isbn_trop_long_invalide(database:Database):
    # résultat attendu : livre NON ajouté car l'isbn est trop long (!= de 10 caractères)
    livre = Livre("082000030099", "Le jeu du trône", 0, 0, 0)
    with pytest.raises(InvalidIsbnException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "Le code isbn doit faire 10 caractères."

def test_ajout_livre_isbn_caractere_invalide(database:Database):
    # résultat attendu : livre NON ajouté car un caractère de l'isbn est invalide
    livre = Livre("08200O0300", "Le jeu du trône", 0, 0, 0)
    with pytest.raises(InvalidIsbnException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "Le code isbn contient des caractères non autorisés."

def test_ajout_livre_duplicata(database:Database):
    # résultat attendu : livre NON ajouté car le code isbn existe déjà
    livre = Livre("0750878851", "Hyrra Pettor", 1, 1, 2)
    with pytest.raises(DuplicataException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "Un livre possède déjà ce code isbn."

def test_ajout_livre_format_inexistant(database:Database):
    # résultat attendu : livre NON ajouté car le format n'existe pas
    livre = Livre("0820000302", "Le jeu du trône", 0, 0, 19795)
    with pytest.raises(MissingDataException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "Le format du livre n'existe pas."

def test_ajout_livre_auteur_inexistant(database:Database):
    # résultat attendu : livre NON ajouté car l'auteur n'existe pas
    livre = Livre("0820000302", "Le jeu du trône", 298877, 0, 0)
    with pytest.raises(MissingDataException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "L'auteur du livre n'existe pas."

def test_ajout_livre_editeur_inexistant(database:Database):
    # résultat attendu : livre NON ajouté car l'éditeur n'existe pas
    livre = Livre("0820000302", "Le jeu du trône", 0, 92673, 0)
    with pytest.raises(MissingDataException) as error:
        resultat = database.livres_insert(livre)
    assert str(error.value) == "L'éditeur du livre n'existe pas."

def test_get_livre_existant(database:Database):
    # résultat attendu : une instance de Livre est retournée
    livre = database.livres_get_by_isbn("0750878851")
    assert isinstance(livre, Livre)

def test_get_livre_inexistant(database:Database):
    # résultat attendu : None est retourné
    livre = database.livres_get_by_isbn("19768")
    assert livre == None