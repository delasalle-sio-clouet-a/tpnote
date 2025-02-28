import json, sys
from flask import Blueprint, current_app
from src.app import database

apiBP = Blueprint('api', __name__)

@apiBP.post("/adherent/all")
def api_adherent_all():
    try:
        data = database.adherents_get_all()
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    except Exception as e:
        current_app.logger.warning(e)
        data = {"message": "Echec de la requête.", "raison": f"{sys.exc_info()[1]}"}
        return current_app.response_class(response=json.dumps(data), status=200, mimetype="application/json")