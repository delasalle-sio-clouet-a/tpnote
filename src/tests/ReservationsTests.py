import pytest
from flask.testing import FlaskClient
from datetime import datetime

from src.classes.CDatabase import Database
from src.classes.CMockMailer import MockMailer

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

from src.exceptions.InvalidFormatException import InvalidFormatException
from src.exceptions.DuplicataException import DuplicataException
from src.exceptions.MissingDataException import MissingDataException

def test_nouvelle_reservation_valide(database:Database):
    # résultat attendu : reservation ajoutée
    dateDebut = datetime(2025, 4, 21, 11, 14, 21)
    dateFin = datetime(2025, 4, 29, 17, 00, 00)
    reservation = Reservation(9, "00475", "0750878851", dateDebut, dateFin, False)
    resultat = database.reservations_insert(reservation)
    assert resultat == True

def test_nouvelle_reservation_adherent_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée car l'adhérent n'existe pas
    dateDebut = datetime(2025, 4, 21, 11, 14, 21)
    dateFin = datetime(2025, 4, 29, 17, 00, 00)
    reservation = Reservation(9, "00100", "0750878851", dateDebut, dateFin, False)
    with pytest.raises(MissingDataException) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "L'adhérent n'existe pas."

def test_nouvelle_reservation_livre_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée car le livre n'existe pas
    dateDebut = datetime(2025, 4, 21, 11, 14, 21)
    dateFin = datetime(2025, 4, 29, 17, 00, 00)
    reservation = Reservation(9, "00475", "0013223100", dateDebut, dateFin, False)
    with pytest.raises(MissingDataException) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "Le livre n'existe pas."

def test_nouvelle_reservation_collision(database:Database):
    # résultat attendu : reservation NON ajoutée car le livre est déjà réservé aux date de début et/ou de fin
    dateDebut = datetime(2025, 1, 5, 11, 00, 00)
    dateFin = datetime(2025, 3, 29, 17, 00, 00)
    reservation = Reservation(9, "00475", "0750878851", dateDebut, dateFin, False)
    with pytest.raises(ValueError) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "Ce livre est déjà réservé dans cet intervalle."

def test_nouvelle_reservation_date_fin_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée car la date de fin est avant la date de début
    dateDebut = datetime(2025, 3, 5, 17, 00, 00)
    dateFin = datetime(2025, 1, 29, 11, 00, 00)
    reservation = Reservation(9, "00475", "0750878851", dateDebut, dateFin, False)
    with pytest.raises(ValueError) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "La date de fin est inférieure à la date de début."

def test_nouvelle_reservation_duree_invalide(database:Database):
    # résultat attendu : reservation NON ajoutée car elle dure plus de quatre mois
    dateDebut = datetime(2025, 7, 2, 13, 15, 00)
    dateFin = datetime(2025, 12, 27, 17, 30, 00)
    reservation = Reservation(9, "00475", "0750878851", dateDebut, dateFin, False)
    with pytest.raises(ValueError) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "La réservation fait plus de quatre mois."

def test_nouvelle_reservation_adherent_maximum(database:Database):
    # résultat attendu : reservation NON ajoutée car l'adhérent a déjà atteint le nombre maximal de réservations en cours (3)
    dateDebut = datetime(2025, 7, 2, 13, 15, 00)
    dateFin = datetime(2025, 8, 17, 15, 00, 00)
    reservation = Reservation(9, "00477", "0941784819", dateDebut, dateFin, False)
    with pytest.raises(ValueError) as error:
        resultat = database.reservations_insert(reservation)
    assert str(error.value) == "L'adhérent a déjà atteint le nombre maximal de réservations en cours."

def test_reservation_rendu_existant(database:Database):
    # résultat attendu : réservation marquée comme rendue
    resultat = database.reservations_set_rendu(0, True)
    assert resultat == True

def test_reservation_rendu_inexistant(database:Database):
    # résultat attendu : réservation NON marquée comme rendu car réservation inexistante
    with pytest.raises(MissingDataException) as error:
        resultat = database.reservations_set_rendu(979898, True)
    assert str(error.value) == "Cette réservation n'existe pas."

def test_reservation_get_en_cours_adherent(database:Database):
    # résultat attendu : 3 instances de réservations sont retournée
    resultat = database.reservations_get_en_cours_by_code_adherent("00477")
    assert len(resultat) == 3

def test_reservation_get_retards_adherent(database:Database):
    # résultat attendu : 2 instances de réservations sont retournées
    resultat = database.reservations_get_retards_by_code_adherent("00475")
    assert len(resultat) == 2

def test_reservation_get_historique_adherent(database:Database):
    # résultat attendu : 4 instances de réservations sont retournées
    resultat = database.reservations_get_all_by_code_adherent("00475")
    assert len(resultat) == 4

def test_reservation_get_retards_tous(database:Database):
    # résultat attendu : 3 instances de réservations sont retournées
    resultat = database.reservations_get_retards_all()
    assert len(resultat) == 6

def test_reservation_envoi_mail_retard(database:Database):
    # résultat attendu : le titre de 2 livres est dans le message du mail
    mailer:MockMailer = MockMailer(database)
    resultat, contenuMail = mailer.envoi_mail_retard("00475")
    assert "Le fond de la bibliothèque" in contenuMail
    assert "Hyrra Pettor" in contenuMail
    

# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)
# A FAIRE : TEST ANNULATION RESERVATION (donc delete)