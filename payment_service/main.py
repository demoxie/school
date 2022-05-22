import logging
import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.config import setup, db_init
from src.routers.common_route import common_router

settings = setup.get_settings()
log = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    await db_init.init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
    await Tortoise.close_connections()


app.include_router(
    common_router,
    prefix=settings.API_PREFIX,
    tags=['public route'],
)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.PAYMENT_SERVICE_SERVER_HOST, port=settings.PAYMENT_SERVICE_SERVER_PORT)
