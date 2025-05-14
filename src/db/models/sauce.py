from sqlalchemy import Column, Integer, String
from src.db.database import Base


class Sauce(Base):
    __tablename__ = 'sauces'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    notes = Column(String)
