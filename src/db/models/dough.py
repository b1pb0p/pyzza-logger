from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base


class DoughObservation(Base):
    __tablename__ = 'dough_observations'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))

    stickiness = Column(Float)
    firmness = Column(Float)
    stretchiness = Column(Float)
    bounce = Column(Float)
    homogeneity = Column(Float)

    recipe = relationship("Recipe")
