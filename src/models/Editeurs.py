from src.app import app, db
from sqlalchemy import ForeignKey

class Editeurs(db.Model):

    __tablename__ = "editeurs"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nom = db.Column(db.String(40), nullable=False)