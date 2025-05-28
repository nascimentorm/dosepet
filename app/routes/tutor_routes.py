from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Tutor
from app import db

tutor_bp = Blueprint('tutor_bp', __name__)

@tutor_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_tutor():
    tutor_id = int(get_jwt_identity())
    tutor = Tutor.query.get(tutor_id)

    if not tutor:
        return jsonify({'message': 'Tutor não encontrado'}), 404

    data = request.get_json()

    # Atualiza apenas os campos permitidos
    tutor.email = data.get('email', tutor.email)
    tutor.phone = data.get('phone', tutor.phone)
    tutor.address = data.get('address', tutor.address)

    db.session.commit()
    return jsonify({'message': 'Dados atualizados com sucesso'}), 200
