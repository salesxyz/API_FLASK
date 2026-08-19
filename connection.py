from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()


def _build_database_url():
    url = os.getenv('URL_DATABASE')
    if url and url.strip():
        return url.strip()

    user = os.getenv('POSTGRE_USER', 'postgres')
    password = os.getenv('POSTGRE_PASSWORD', 'postgres')
    host = os.getenv('POSTGRE_HOST', 'localhost')
    port = os.getenv('POSTGRE_PORT', '5432')
    name = os.getenv('POSTGRE_DB', 'api_flask')
    return f'postgresql+psycopg://{user}:{password}@{host}:{port}/{name}'


class Config:
    SQLALCHEMY_DATABASE_URI = _build_database_url()
    SQLALCHEMY_TRACK_NOTIFICATIONS = False


config = Config()