import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or ''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/emergency'
    SQLALCHEMY_TRACK_MODIFICATIONS = False