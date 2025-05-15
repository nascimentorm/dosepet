from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import db

tutor_bp = Blueprint('tutor_bp', __name__)

@tutor_bp.route('/update', methods=['PUT'])
@login_required
def update_tutor():
    data = request.get_json()

    # Atualiza apenas os campos permitidos
    current_user.email = data.get('email', current_user.email)
    current_user.phone = data.get('phone', current_user.phone)
    current_user.address = data.get('address', current_user.address)

    db.session.commit()
    return jsonify({'message': 'Dados atualizados com sucesso'}), 200
