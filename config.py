import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:a1e2bdrn@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
