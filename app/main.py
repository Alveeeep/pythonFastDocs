from fastapi import FastAPI, Request
from app.routers import search
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from app.database.models import Base
from app.database.database import engine



origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "https://zakupki.tatar/",
    "https://alvir.misalimov.fvds.ru/",
    "https://localhost",
    "https://localhost:8888",
    "https://zakupki.tatar/privet-bro/alvir-test/",
    "https://localhost:80",
    "https://localhost:8000"

]
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization"],
    )
]

app = FastAPI(middleware=middleware)
app.include_router(search.router)
Base.metadata.create_all(bind=engine)
