from src.app import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Livres(Base):

    __tablename__ = "livres"

    code_isbn = Column(String(10), primary_key=True, nullable=False)

    titre = Column(String(10), nullable=False)

    id_auteur = Column(Integer, ForeignKey("auteurs.id"), nullable=False)
    id_editeur = Column(Integer, ForeignKey("editeurs.id"), nullable=False)
    id_format = Column(Integer, ForeignKey("formats.id"), nullable=False)