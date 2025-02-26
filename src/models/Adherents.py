from src.app import app, db
from sqlalchemy import ForeignKey

class Livres(db.Model):

    __tablename__ = "livres"

    code_adherent = db.Column(db.String(5), primary_key=True, nullable=False)

    nom = db.Column(db.String(40), nullable=False)
    prenom = db.Column(db.String(40), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    civilite = db.Column(db.Boolean, nullable=False)