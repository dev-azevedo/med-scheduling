from fastapi import FastAPI
from src.routers.medical_specialties_routers import router as router_medical_specialties
from src.routers.doctors_routers import router as router_doctors
from src.infra.create_tables import create_tables
from src.config.scalar import router as router_scalar

create_tables()

app = FastAPI(    
    title="Med Scheduling",
    description="Sistema de agendamento de consultas médicas",
    version="0.0.1",
    contact={
        "name": "Jhonatan Azevedo",
        "email": "dev.azevedo@outlook.com",
    },)

app.include_router(router_scalar)
app.include_router(router_medical_specialties)
app.include_router(router_doctors)