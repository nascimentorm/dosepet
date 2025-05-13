from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        
        from app.routes.auth_routes import auth_bp
        app.register_blueprint(auth_bp)

        from app.routes.pet_routes import pet_bp
        app.register_blueprint(pet_bp)

    return app
