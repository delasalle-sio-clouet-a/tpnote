from sqlalchemy import ForeignKey
from src.app import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Auteurs(Base):

    __tablename__ = "auteurs"

    id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String(40), nullable=False)
    prenom = Column(String(40), nullable=False)