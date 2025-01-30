from fastapi import FastAPI
from src.routers.medical_specialties_routers import router as router_medical_specialties
from src.infra.database import engine
from src.models import medical_specialties_model

medical_specialties_model.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(router_medical_specialties)