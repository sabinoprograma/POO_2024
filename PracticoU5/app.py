from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import Sucursal,Transporte,Paquete,Repartidor
from config import db,SQLALCHEMY_DATABASE_URI,SQLALCHEMY_TRACK_MODIFICATIONS,SECRET_KEY
import uuid,pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sucursal', methods=['GET', 'POST'])
def sucursal(): # funcion para seleccionar la sucursal
    sucursales = Sucursal.query.order_by(Sucursal.numero.asc()).all()
    if request.method == 'POST':
        id_sucursal = request.form['sucursal']
        session['id_sucursal'] = id_sucursal
        return redirect(url_for('despachante'))
    return render_template('sucursal.html',sucursales=sucursales)

@app.route('/despachante', methods=['GET'])
def despachante(): #dashboard del despachante
    id_sucursal = session.get('id_sucursal')
    return render_template('despachante.html', id_sucursal=id_sucursal)

@app.route('/repartidor')
def repartidor():
    return render_template('repartidor.html')

# funcionalidad 1 para registrar paquetes como despachante
@app.route('/registrar_paquete', methods=['GET', 'POST'])
def registrar_paquete():
    sucursales = Sucursal.query.all()
    sucursal_actual = session.get('id_sucursal')
    if request.method == 'POST':
        peso = request.form['peso']
        nomdestino = request.form['nomdestino']
        dirdestino = request.form['dirdestino']
        observaciones = request.form['observaciones']
        if not sucursal_actual:
            flash('La sucursal es obligatoria.', 'error')
            return redirect(url_for('registrar_paquete'))
        try:
            numeroenvio = str(uuid.uuid4())[:8]
            nuevo_paquete = Paquete(
                numeroenvio=numeroenvio,
                peso=peso,
                nomdestino=nomdestino,
                dirdestino=dirdestino,
                idsucursal=int(sucursal_actual),
                entregado=False,
                observaciones=observaciones
            )
            db.session.add(nuevo_paquete)
            db.session.commit()
            flash('Paquete registrado correctamente.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar el paquete: {e}', 'error')
        return redirect(url_for('registrar_paquete'))
    return render_template('registrar_paquete.html', sucursal_actual=int(sucursal_actual), sucursales=sucursales)

# funcionalidad 3 
@app.route('/sucursal_salida', methods=['GET', 'POST'])
def sucursal_salida(): # seleccionar la sucursal de salida
    sucursales = Sucursal.query.order_by(Sucursal.numero.asc()).all()
    sucursal_actual = session.get('id_sucursal')
    if request.method == 'POST':
        sucursal_salida = request.form['sucursal_salida']
        session['sucursal_salida'] = sucursal_salida
        return redirect(url_for('transporte_salida'))
    return render_template('sucursal_salida.html', sucursales=sucursales, sucursal_actual=int(sucursal_actual))

#funcionalidad 3 para asignar paquetes a un transporte de llegada
@app.route('/transporte_salida', methods=['GET', 'POST'])
def transporte_salida(): #asignar paquetes a un transporte de salida
    sucursal_actual = session.get('id_sucursal')
    sucursal_salida = session.get('sucursal_salida')
    if request.method == 'POST':
        idsucursal = sucursal_salida
        paquetes_ids = request.form.getlist('paquetes')
        numerotransporte = str(uuid.uuid4())[:8]
        nuevo_transporte = Transporte(
            numerotransporte = numerotransporte,
            fechahorasalida= datetime.now(),
            idsucursal = idsucursal
        )
        db.session.add(nuevo_transporte)
        db.session.commit()
        for paquete_id in paquetes_ids: #asignar paquetes al transporte
            paquete = Paquete.query.get(paquete_id)
            paquete.idtransporte = nuevo_transporte.id
            db.session.commit()
        flash('Salida de transporte registrada exitosamente.', 'success')
        return redirect(url_for('transporte_salida'))
    sucursales = Sucursal.query.all()
    paquetes = Paquete.query.filter_by(entregado=False, idtransporte=None).all()
    return render_template('transporte_salida.html', sucursales=sucursales, paquetes=paquetes, sucursal_actual=int(sucursal_actual),sucursal_salida=int(sucursal_salida))

#funcionalidad 4 para registrar la llegada de un transporte
@app.route('/transporte_llegada', methods=['GET', 'POST'])
def transporte_llegada(): #registrar la llegada de un transporte
    sucursal_actual = session.get('id_sucursal')
    if request.method == 'POST':
        idtransporte = request.form.get('idtransporte')
        if not idtransporte:
            flash('No se ha seleccionado un transporte.', 'error')
            return redirect(url_for('transporte_llegada'))
        transporte = Transporte.query.get(idtransporte)
        if not transporte:
            flash('Transporte no encontrado.', 'error')
            return redirect(url_for('transporte_llegada'))
        try:
            transporte.fechahorallegada = datetime.now()
            db.session.commit()
            flash('Llegada de transporte registrada exitosamente.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar la llegada del transporte:', 'error')
        return redirect(url_for('transporte_llegada'))
    transportes = Transporte.query.filter_by(fechahorallegada=None, idsucursal=sucursal_actual).all()
    sucursales = Sucursal.query.all()
    return render_template('transporte_llegada.html', transportes=transportes, sucursales=sucursales, sucursal_actual=int(sucursal_actual))

if __name__ == '__main__':
    app.run(debug=True)