from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base


class BakeDetails(Base):
    __tablename__ = 'bake_details'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    oven_model = Column(String)
    average_insert_temp = Column(Float)
    rise_score = Column(Float)
    elasticity = Column(Float)
    pie_size = Column(Float)

    recipe = relationship("Recipe")
