import asyncio
import uvicorn
from fastapi import FastAPI, APIRouter
from config import Config

from repositories import Repository
from services import Service
from handlers import Handler

import logging

logging.basicConfig(level=logging.INFO)


Config.set()

repository = Repository()
service = Service(repository)
handler = Handler(service)

app = FastAPI(title="Donor")
handler.register(app)


def make_migrations():
    # from repositories.mysql import Base
    # Base.metadata.drop_all(repository.mysql)
    # Base.metadata.create_all(repository.mysql)
    pass


if __name__ == "__main__":
    make_migrations()
    uvicorn.run(app="main:app", reload=True, port=80)
