from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    total_flour = Column(Float, nullable=False)
    water = Column(Float, nullable=False)
    salt = Column(Float, nullable=False)
    yeast_weight = Column(Float, nullable=False)
    oil = Column(Float, nullable=True)
    ball_weight = Column(Float, nullable=False)
    num_balls = Column(Integer, nullable=False)

    flours = relationship("FlourUse", back_populates="recipe")
    yeast = relationship("Yeast", back_populates="recipe", uselist=False)
    balls = relationship("Ball", back_populates="recipe")


class FlourUse(Base):
    __tablename__ = 'flour_use'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    flour_type = Column(String, nullable=False)
    flour_weight = Column(Float, nullable=False)
    grind_level = Column(String)

    recipe = relationship("Recipe", back_populates="flours")


class Yeast(Base):
    __tablename__ = 'yeast'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    yeast_type = Column(String, nullable=False)
    expiry_date = Column(String)

    recipe = relationship("Recipe", back_populates="yeast")
