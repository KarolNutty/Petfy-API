from fastapi import FastAPI
from app.routes.pet import router
from app.core.database import create_db

app = FastAPI(title="Petfy API 🐾")

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(router)


