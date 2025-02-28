from sqlalchemy import ForeignKey
from src.app import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Adherents(Base):

    __tablename__ = "adherents"

    code_adherent = Column(String(5), primary_key=True, nullable=False)

    nom = Column(String(40), nullable=False)
    prenom = Column(String(40), nullable=False)
    date_naissance = Column(Date, nullable=False)
    civilite = Column(Boolean, nullable=False)
    email = Column(String(75), nullable=False)