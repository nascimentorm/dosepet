from . import db, bcrypt
from datetime import datetime

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_tutor = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    pets = db.relationship('Pet', backref='tutor', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Veterinarian(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_veterinarian = db.Column(db.String(120), nullable=False)
    crmv = db.Column(db.String(20), unique=True, nullable=False)
    clinic = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_pet = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    race = db.Column(db.String(50), nullable=True)
    colors = db.Column(db.String(100), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False) 
    photo_pet = db.Column(db.String(200))
    tutor_cpf = db.Column(db.String(14), db.ForeignKey('tutor.cpf'), nullable=False)

    applications = db.relationship('Application', backref='pet', lazy=True)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    veterinarian_id = db.Column(db.Integer, db.ForeignKey('veterinarian.id'), nullable=False)
    
    vaccine_applied = db.Column(db.String(100))
    photo_label = db.Column(db.String(200))
    date_vaccine = db.Column(db.Date, nullable=True)

    vermifuge_applied = db.Column(db.String(100))
    photo_vermifuge = db.Column(db.String(200))
    date_vermifuge = db.Column(db.Date, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
