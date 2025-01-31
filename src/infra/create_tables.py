from src.infra.database import engine
from src.models import medical_specialties_model, doctors_model, doctor_medical_specialties_model

def create_tables():
    medical_specialties_model.Base.metadata.create_all(engine)
    doctors_model.Base.metadata.create_all(engine)
    doctor_medical_specialties_model.Base.metadata.create_all(engine)