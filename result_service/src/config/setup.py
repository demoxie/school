from pathlib import Path
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings
from functools import lru_cache
import cloudinary
import os
from dotenv import load_dotenv

dotenv_path = Path('', '.env')

load_dotenv(dotenv_path=dotenv_path)


class Settings(BaseSettings):
    API_PREFIX: str = os.environ.get("API_PREFIX")
    PG_HOST: str = os.environ.get("PG_HOST")
    RESULT_SERVICE_SERVER_PORT = int(os.environ.get("RESULT_SERVICE_SERVER_PORT"))
    RESULT_SERVICE_SERVER_HOST = str(os.environ.get("RESULT_SERVICE_SERVER_HOST"))
    PG_USERNAME = str(os.environ.get("PG_USERNAME"))
    SSL_MODE = str(os.environ.get("SSL_MODE"))
    PG_PASSWORD = str(os.getenv("PG_PASSWORD"))
    RESULT_SERVICE_DB = str(os.getenv("RESULT_SERVICE_DB"))
    BASE_URL = 'https://{}'.format(RESULT_SERVICE_SERVER_HOST)
    DATABASE_URL = 'postgres://{}:{}@{}/{}'.format(PG_USERNAME, PG_PASSWORD, PG_HOST, RESULT_SERVICE_DB)

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
    TEMPLATE_FOLDER=Path('src/templates/')
)

cloudinary.config(
    cloud_name="hnduusros",
    api_key="927131722149478",
    api_secret="he5lFnOeoeRDBmV9z9QKCTxhLn0"
)


@lru_cache()
def get_settings():
    return Settings()
