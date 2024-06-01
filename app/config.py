import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or ''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:@localhost/emergency'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('TRACK_MODIFICATIONS') or False
    DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL') or ''
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID') or ''
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') or ''