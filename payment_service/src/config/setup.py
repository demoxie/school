import os
from functools import lru_cache
from pathlib import Path
import cloudinary
from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_PREFIX: str = os.environ.get("API_PREFIX")
    HOST: str = os.environ.get("PG_HOST")
    PG_PORT: str = os.environ.get("PG_PORT")
    PAYMENT_SERVICE_SERVER_PORT = int(os.environ.get("PAYMENT_SERVICE_SERVER_PORT"))
    PAYMENT_SERVICE_SERVER_HOST = str(os.environ.get("PAYMENT_SERVICE_SERVER_HOST"))
    PG_USERNAME = str(os.environ.get("PG_USERNAME"))
    SSL_MODE = str(os.environ.get("SSL_MODE"))
    PG_PASSWORD = str(os.getenv("PG_PASSWORD"))
    PAYMENT_SERVICE_DB = str(os.getenv("PAYMENT_SERVICE_DB"))
    BASE_URL = 'https://{}'.format(PAYMENT_SERVICE_SERVER_HOST)
    DATABASE_URL = 'postgres://{}:{}@{}:{}/{}'.format(PG_USERNAME, PG_PASSWORD, HOST, PG_PORT, PAYMENT_SERVICE_DB)

    MODELS = [
        'src.models.user_model'
    ]

    class Config:
        case_sensitive: bool = True


conf = ConnectionConfig(
    MAIL_USERNAME='shadrachadamuul@gmail.com',
    MAIL_PASSWORD='Ubandomaadamu@24',
    MAIL_FROM='shadrachadamuul@gmail.com',
    MAIL_PORT=587,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False,
    TEMPLATE_FOLDER=Path('src/templates'),
)

cloudinary.config(
    cloud_name="hnduusros",
    api_key="927131722149478",
    api_secret="he5lFnOeoeRDBmV9z9QKCTxhLn0"
)


@lru_cache()
def get_settings():
    return Settings()
