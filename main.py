from fastapi import FastAPI
from src.routers.medical_specialties_routers import router as router_medical_specialties
from src.infra.create_tables import create_tables

create_tables()

app = FastAPI()

app.include_router(router_medical_specialties)