from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    overall = Column(Float)
    taste = Column(Float)
    texture = Column(Float)

    recipe = relationship("Recipe")
