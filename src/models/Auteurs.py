from src.app import app, db
from sqlalchemy import ForeignKey

class Auteurs(db.Model):

    __tablename__ = "auteurs"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(40), nullable=False)
    prenom = db.Column(db.String(40), nullable=False)