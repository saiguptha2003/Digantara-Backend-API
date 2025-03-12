import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///digantara.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
