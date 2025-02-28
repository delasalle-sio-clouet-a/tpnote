import json, sys
from flask import Blueprint, current_app, request
from src.app import database

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

apiBP = Blueprint('api', __name__)

@apiBP.get("/adherents/all")
def api_adherent_all():
    try:
        resultat = database.adherents_get_all()
        data = []
        for uneLigne in resultat:
            dataLigne = {}
            dataLigne["code"] = uneLigne.code_adherent
            dataLigne["nom"] = uneLigne.nom
            dataLigne["prenom"] = uneLigne.prenom
            dataLigne["date_naissance"] = uneLigne.date_naissance.strftime("%Y-%m-%d")
            dataLigne["email"] = uneLigne.email
            dataLigne["civilite"] = uneLigne.civilite
            data.append(dataLigne)

        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    except Exception as e:
        current_app.logger.warning(e)
        data = {"message": "Echec de la requête.", "raison": f"{sys.exc_info()[1]}"}
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    
@apiBP.get("/adherents/<code>")
def api_adherent_by_code(code):
    try:
        resultat = database.adherents_get_by_code(code)
        if(resultat != None):
            data = {}
            data["code"] = resultat.code_adherent
            data["nom"] = resultat.nom
            data["prenom"] = resultat.prenom
            data["date_naissance"] = resultat.date_naissance.strftime("%Y-%m-%d")
            data["email"] = resultat.email
            data["civilite"] = resultat.civilite
        else:
            data = None
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    except Exception as e:
        current_app.logger.warning(e)
        data = {"message": "Echec de la requête.", "raison": f"{sys.exc_info()[1]}"}
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    
@apiBP.post("/adherents/ajouter")
def api_adherent_ajouter():
    if(request.form):
        code = request.form.get("code")
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
        dateNaissance = request.form.get("date_naissance")
        email = request.form.get("email")
        civilite = bool(request.form.get("civilite"))

        try:
            adherent = Adherent(code, nom, prenom, dateNaissance, civilite, email)
            data = database.adherents_insert(adherent)
            return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
        except Exception as e:
            current_app.logger.warning(e)
            data = {"message": "Echec de la requête.", "raison": f"{sys.exc_info()[1]}"}
            return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")

    else:
        data = {"message": "Echec de la requête.", "raison": "Données manquantes."}
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")