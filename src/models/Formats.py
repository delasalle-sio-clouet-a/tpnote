from src.app import app, db
from sqlalchemy import ForeignKey

class Formats(db.Model):

    __tablename__ = "formats"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    libelle = db.Column(db.String(40), nullable=False)