from pathlib import Path

from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings
from functools import lru_cache
import cloudinary
import os
from dotenv import load_dotenv

dotenv_path = Path('.env')

load_dotenv(dotenv_path=dotenv_path)


class Settings(BaseSettings):
    SECRET_KEY = str(os.environ.get("SECRET_KEY"))
    APP_NAME = str(os.environ.get("APP_NAME"))
    REGISTRATION_TOKEN_LIFETIME = int(os.environ.get(
        "REGISTRATION_TOKEN_LIFETIME"))
    ACCESS_TOKEN_TIME = int(os.environ.get("ACCESS_TOKEN_TIME"))
    PASSWORD_RESET_TOKEN_LIFETIME = int(os.environ.get(
        "PASSWORD_RESET_TOKEN_LIFETIME"))
    TOKEN_ALGORITHM = str(os.environ.get("TOKEN_ALGORITHM"))
    SERVER_HOST = str(os.environ.get("SERVER_HOST"))
    USER_SERVICE_DB = str(os.getenv("PAYMENT_SERVICE_DB"))
    BASE_URL = 'https://{}'.format(SERVER_HOST)

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
    TEMPLATE_FOLDER=os.path.join('', 'templates')
)

cloudinary.config(
    cloud_name="hnduusros",
    api_key="927131722149478",
    api_secret="he5lFnOeoeRDBmV9z9QKCTxhLn0"
)


@lru_cache()
def get_settings():
    return Settings()
