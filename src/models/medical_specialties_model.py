from sqlalchemy import Column, Integer, String
from .base_model import BaseModel, Base


class MedicalSpecialties(Base, BaseModel):
    __tablename__ = "medical_specialties"
    
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)