from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.db.database import Base


class Proofing(Base):
    __tablename__ = 'proofing'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    stage = Column(String)
    temperature = Column(Float)
    hours = Column(Float)

    recipe = relationship("Recipe")


class TimeLog(Base):
    __tablename__ = 'time_logs'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    start_time = Column(DateTime)
    end_time = Column(DateTime)
    autolyse_rest = Column(Float)

    recipe = relationship("Recipe")


class TemperatureLog(Base):
    __tablename__ = 'temperature_logs'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    room_temp = Column(Float)
    water_temp = Column(Float)
    after_knead_temp = Column(Float)
    after_autolyse_temp = Column(Float)

    recipe = relationship("Recipe")
