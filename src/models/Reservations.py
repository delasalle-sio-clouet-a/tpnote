from src.app import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Reservations(Base):

    __tablename__ = "reservations"

    code_adherent = Column(String(5), ForeignKey("adherents.code_adherent"), primary_key=True, nullable=False)
    code_isbn = Column(String(10), ForeignKey("livres.code_isbn"), primary_key=True, nullable=False)
    date_heure_debut = Column(DateTime, nullable=False)
    date_heure_fin = Column(DateTime, nullable=True)
    rendu = Column(Boolean, nullable=False)