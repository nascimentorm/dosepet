from flask import Blueprint, request, jsonify
from app.models import db, Veterinarian

veterinarian_bp = Blueprint('veterinarian_bp', __name__)

#cadastro de veterinario

@veterinarian_bp.route('/veterinarians', methods=['POST'])
def register_veterinarian():
    data = request.get_json()

    if Veterinarian.query.filter_by(crmv=data['crmv']).first():
        return jsonify({"error": "Veterinário já cadastrado com este CRMV"}), 400

    veterinarian = Veterinarian(
        name_veterinarian=data['name_veterinarian'],
        crmv=data['crmv'],
        clinic=data['clinic']
    )

    db.session.add(veterinarian)
    db.session.commit()

    return jsonify({"message": "Veterinário cadastrado com sucesso!"}), 201
