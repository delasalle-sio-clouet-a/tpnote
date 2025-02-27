from src.app import app, db
from sqlalchemy import ForeignKey

class Reservations(db.Model):

    __tablename__ = "reservations"

    code_adherent = db.Column(db.String(5), ForeignKey("adherents.code_adherent"), primary_key=True, nullable=False)
    code_isbn = db.Column(db.String(10), ForeignKey("livres.code_isbn"), primary_key=True, nullable=False)
    date_heure_debut = db.Column(db.DateTime, nullable=False)
    date_heure_fin = db.Column(db.DateTime, nullable=True)
    rendu = db.Column(db.Boolean, nullable=False)