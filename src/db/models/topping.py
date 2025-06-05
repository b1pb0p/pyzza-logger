from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class Topping(Base):
    __tablename__ = 'topping'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, default='generic')
    weight = Column(Float, nullable=False)
    notes = Column(String)

    nutrition_id = Column(Integer, ForeignKey('nutritional_value.id'), unique=True)
    nutrition = relationship("NutritionalValue", back_populates="topping", uselist=False)
