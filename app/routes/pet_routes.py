from flask import Blueprint, request, jsonify
from app.models import db, Pet, Tutor
from datetime import datetime, date

pet_bp = Blueprint('pet_bp', __name__)

@pet_bp.route('/pets', methods=['POST'])
def register_pet():
    data = request.get_json()

    # Buscar o tutor pelo CPF
    tutor = Tutor.query.filter_by(cpf=data['tutor_cpf']).first()
    if not tutor:
        return jsonify({'error': 'Tutor não encontrado'}), 404

    try:
        # Calcular a idade do pet
        birth_date = datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Criar o pet com o tutor encontrado pelo CPF
        pet = Pet(
            name_pet=data['name_pet'],
            weight=data['weight'],
            race=data.get('race'),
            colors=data.get('colors'),
            date_of_birth=birth_date,
            age=age,
            sex=data['sex'],
            tutor_cpf=tutor.cpf  # Associar o pet pelo CPF do tutor
        )

        db.session.add(pet)
        db.session.commit()

        return jsonify({"message": "Pet cadastrado com sucesso!", "pet_id": pet.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
