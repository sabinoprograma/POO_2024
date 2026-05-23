from app import app, db
from models import Paquete, Sucursal, Transporte, Repartidor

with app.app_context():
    db.create_all()
    print("Base de datos creada con éxito.")