from flask import Blueprint, request, jsonify
from app.models import Tutor, db
from app import bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

#Registro de Tutor
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if Tutor.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400

    tutor = Tutor(
        name_tutor=data['name_tutor'],
        cpf=data['cpf'],
        email=data['email'],
        phone=data['phone'],
        address=data.get('address', '')
    )
    tutor.set_password(data['password'])

    db.session.add(tutor)
    db.session.commit()

    return jsonify({"message": "Cadastro realizado com sucesso!"}), 201

# Login de Tutor
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    tutor = Tutor.query.filter_by(email=data['email']).first()

    if tutor and tutor.check_password(data['password']):
        access_token = create_access_token(identity=str(tutor.id))

        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Email ou senha inválidos"}), 401
