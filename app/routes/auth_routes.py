from flask import Blueprint, request, jsonify
from app.models import Tutor, db
from app import bcrypt

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
        return jsonify({"message": "Login realizado com sucesso!"}), 200

    return jsonify({"error": "Email ou senha inválidos"}), 401

from app.models import Tutor, Veterinarian, db
from app import bcrypt

# Registro de veterinário
@auth_bp.route('/veterinarian/register', methods=['POST'])
def register_veterinarian():
    data = request.get_json()

    if Veterinarian.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email já cadastrado"}), 400

    veterinarian = Veterinarian(
        name_veterinarian=data['name_veterinarian'],
        crmv=data['crmv'],
        clinic=data['clinic'],
        email=data['email']
    )
    veterinarian.set_password(data['password'])

    db.session.add(veterinarian)
    db.session.commit()

    return jsonify({"message": "Veterinário cadastrado com sucesso!"}), 201


# Login de veterinário
@auth_bp.route('/veterinarian/login', methods=['POST'])
def login_veterinarian():
    data = request.get_json()

    veterinarian = Veterinarian.query.filter_by(email=data['email']).first()
    if veterinarian and veterinarian.check_password(data['password']):
        return jsonify({
            "message": "Login realizado com sucesso!",
            "veterinarian_id": veterinarian.id,
            "name_veterinarian": veterinarian.name_veterinarian
        }), 200

    return jsonify({"error": "Email ou senha inválidos"}), 401
