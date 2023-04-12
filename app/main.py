from fastapi import FastAPI, Request
from .routers import search


app = FastAPI()

app.include_router(search.router)




