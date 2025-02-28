from src.app import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime

class Formats(Base):

    __tablename__ = "formats"

    id = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(40), nullable=False)