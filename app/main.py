from fastapi import FastAPI, Request
from .routers import search
from fastapi.middleware.cors import CORSMiddleware
from app.database.models import Base
from app.database.database import engine
import uvicorn


app = FastAPI()

app.include_router(search.router)
Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:8080"
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin"],
)

