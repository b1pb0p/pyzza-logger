from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

from src.db.database import Base


class NutritionalValue(Base):
    __tablename__ = 'nutritional_value'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    calories = Column(Float, default=0)
    protein = Column(Float, default=0)
    carbs = Column(Float, default=0)
    fat = Column(Float, default=0)
    fiber = Column(Float, default=0)

    flour = relationship("Flour", back_populates="nutrition", uselist=False)
    sauce = relationship("Sauce", back_populates="nutrition", uselist=False)
    topping = relationship("Topping", back_populates="nutrition", uselist=False)
