from sqlalchemy import Column, Integer, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from src.db.database import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    total_flour = Column(Float, nullable=False)
    water = Column(Float, nullable=False)
    salt = Column(Float, nullable=False)
    yeast_weight = Column(Float, nullable=False)
    oil = Column(Float, nullable=True)
    ball_weight = Column(Float, nullable=False)
    num_balls = Column(Integer, nullable=False)
    notes = Column(String)

    flours = relationship("FlourUse", back_populates="recipe")
    yeast = relationship("Yeast", back_populates="recipe", uselist=False)
    balls = relationship("Ball", back_populates="recipe")


class FlourUse(Base):
    __tablename__ = 'flour_use'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    flour_id = Column(Integer, ForeignKey('flour.id'), nullable=False)
    flour_weight = Column(Float, nullable=False)

    recipe = relationship("Recipe", back_populates="flours")
    flour = relationship("Flour", back_populates="flour_uses")


class Flour(Base):
    __tablename__ = 'flour'

    id = Column(Integer, primary_key=True)
    manufacturer = Column(String, nullable=False)
    type = Column(String, nullable=False)
    grind_level = Column(String, default='00')

    nutrition_id = Column(Integer, ForeignKey('nutritional_value.id'), unique=True)
    nutrition = relationship("NutritionalValue", back_populates="flour", uselist=False)

    flour_uses = relationship("FlourUse", back_populates="flour")


class Yeast(Base):
    __tablename__ = 'yeast'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    yeast_type = Column(String, nullable=False)
    expiry_date = Column(String)

    recipe = relationship("Recipe", back_populates="yeast")
