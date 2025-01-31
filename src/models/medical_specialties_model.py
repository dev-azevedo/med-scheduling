from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_model import BaseModel, Base
from .doctor_medical_specialties_model import DoctorMedicalSpecialties


class MedicalSpecialties(Base, BaseModel):
    __tablename__ = "medical_specialties"
    
    name = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    
    doctors = relationship("Doctors", secondary=DoctorMedicalSpecialties.__tablename__, back_populates="medical_specialties")