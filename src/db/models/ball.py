from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.db.database import Base


class Ball(Base):
    __tablename__ = 'balls'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ball_number = Column(Integer, nullable=False)

    sauce_id = Column(Integer, ForeignKey('sauces.id'), nullable=True)
    taste_score = Column(Float, nullable=True)

    recipe = relationship("Recipe", back_populates="balls")
    sauce = relationship("Sauce")
    toppings = relationship("BallTopping", back_populates="ball")


class BallTopping(Base):
    __tablename__ = 'ball_toppings'

    id = Column(Integer, primary_key=True)
    ball_id = Column(Integer, ForeignKey('balls.id'))
    topping_id = Column(Integer, ForeignKey('toppings.id'))

    ball = relationship("Ball", back_populates="toppings")
    topping = relationship("Topping")
