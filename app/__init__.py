from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.auth.routes import auth_bp
    from app.emergency.routes import emergency_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(emergency_bp, url_prefix='/emergency')

    return app