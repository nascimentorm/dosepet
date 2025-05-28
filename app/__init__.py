from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Certifique-se de que o caminho está correto

    # Configuração da chave secreta para JWT
    app.config['JWT_SECRET_KEY'] = 'marioladoce'  

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        # Registrar os blueprints
        from app.routes.auth_routes import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.routes.pet_routes import pet_bp
        app.register_blueprint(pet_bp)

        # Certifique-se de registrar o blueprint do tutor, se existir
        from app.routes.tutor_routes import tutor_bp
        app.register_blueprint(tutor_bp, url_prefix='/tutor')

    return app
