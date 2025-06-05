from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.db.database import Base


class Sauce(Base):
    __tablename__ = 'sauce'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    notes = Column(String)

    nutrition_id = Column(Integer, ForeignKey('nutritional_value.id'), unique=True)
    nutrition = relationship("NutritionalValue", back_populates="sauce", uselist=False)
