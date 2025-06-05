from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.db.database import Base


class Ball(Base):
    __tablename__ = 'ball'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    ball_number = Column(Integer, nullable=False)

    sauce_id = Column(Integer, ForeignKey('sauce.id'), nullable=True)
    # taste_score = Column(Float, nullable=True)

    recipe = relationship("Recipe", back_populates="balls")
    sauce = relationship("Sauce")
    topping = relationship("BallTopping", back_populates="ball")


class BallTopping(Base):
    __tablename__ = 'ball_topping'

    id = Column(Integer, primary_key=True)
    ball_id = Column(Integer, ForeignKey('ball.id'))
    topping_id = Column(Integer, ForeignKey('topping.id'))

    ball = relationship("Ball", back_populates="topping")
    topping = relationship("Topping")
