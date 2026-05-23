from config import db

class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.String(20), unique=True, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestino = db.Column(db.String(50), nullable=False)
    dirdestino = db.Column(db.String(100), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String(200))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))