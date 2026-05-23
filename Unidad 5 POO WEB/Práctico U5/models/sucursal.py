from config import db

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    provincia = db.Column(db.String(50), nullable=False)
    localidad = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    transportes = db.relationship('Transporte', backref='sucursal', cascade='all, delete-orphan')
    repartidores = db.relationship('Repartidor', backref='sucursal', cascade='all, delete-orphan')
    paquetes = db.relationship('Paquete', backref='sucursal', cascade='all, delete-orphan')