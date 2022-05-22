import ssl

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from base_config.setup import get_settings

ctx = ssl.create_default_context()

ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
settings = get_settings()


async def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={"models": settings.MODELS},
        generate_schemas=True,
        add_exception_handlers=True,
    )
