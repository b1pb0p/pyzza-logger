from sqlalchemy import Column, Integer, String
from src.db.database import Base


class Topping(Base):
    __tablename__ = 'toppings'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, default='generic')
    notes = Column(String)
