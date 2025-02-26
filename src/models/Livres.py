from src.app import app, db
from sqlalchemy import ForeignKey

class Livres(db.Model):

    __tablename__ = "livres"

    code_isbn = db.Column(db.String(10), primary_key=True, nullable=False)

    titre = db.Column(db.String(10), nullable=False)

    id_auteur = db.Column(db.Integer, ForeignKey("auteurs.id"), nullable=False)
    id_editeur = db.Column(db.Integer, ForeignKey("editeurs.id"), nullable=False)
    id_format = db.Column(db.Integer, ForeignKey("formats.id"), nullable=False)