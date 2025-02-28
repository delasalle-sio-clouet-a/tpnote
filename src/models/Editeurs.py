from src.app import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Editeurs(Base):

    __tablename__ = "editeurs"

    id = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String(40), nullable=False)