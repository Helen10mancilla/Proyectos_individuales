from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
from dotenv import load_dotenv
from datetime import datetime

import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configura la conexión a tu base de datos MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # <- cámbialo
        password="",# <- cámbialo
        database="mi_sitio"
    )
conexion = conectar_db()
cursor = conexion.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']

        conn = conectar_db()
        cursor = conn.cursor()

        # Verifica si el correo ya existe
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        existente = cursor.fetchone()

        if existente:
            cursor.close()
            conn.close()
            # Aquí en vez de devolver error normal, redirigimos a una página especial
            return render_template('ya_registrado.html', correo=correo)
        else:
            # Insertamos al nuevo usuario
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, password) VALUES (%s, %s, %s)",
                (nombre, correo, password)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(f'/seleccionar_rol?correo={correo}')
    
    return render_template('registro.html')

from flask import session

app.secret_key = "secreto_ninja"  # clave para sesiones

@app.route('/seleccionar_rol', methods=['POST'])
def seleccionar_rol():
    rol = request.form['rol']
    correo = session.get('correo')

    if not correo:
        return redirect(url_for('login'))

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET rol = %s WHERE correo = %s", (rol, correo))
    conn.commit()
    cursor.close()
    conn.close()

    session['rol'] = rol

    if rol == 'administrador':
        return redirect(url_for('asociar_negocio'))
    else:
        return redirect(url_for('pagina_usuario'))

from flask import session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND password = %s", (correo, password))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario:
            session['correo'] = usuario['correo']
            session['rol'] = usuario['rol']
            session['nombre_negocio'] = usuario.get('nombre_negocio')

            if usuario['rol'] == 'administrador':
                if usuario.get('nombre_negocio'):
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('asociar_negocio'))
            else:
                return redirect(url_for('pagina_usuario'))

        else:
            return "Correo o contraseña incorrectos"

    return render_template('login.html')


@app.route('/pagina_usuario')
def pagina_usuario():
    if 'correo' in session and session.get('rol') == 'usuario':
        return render_template('pagina_usuario.html')
    else:
        return redirect(url_for('login'))

@app.route('/asociar_negocio', methods=['GET', 'POST'])
def asociar_negocio():
    global conexion

    cursor = conexion.cursor(dictionary=True)
    
    # Primero traemos la lista de negocios para el select o lo que sea
    cursor.execute("SELECT * FROM negocios")
    negocios = cursor.fetchall()

    if request.method == 'POST':
        nuevo_nombre = request.form.get('nuevo_nombre')
        # Otras variables que necesites, tipo descripción, etc.

        # Validar si ya existe ese negocio
        cursor.execute("SELECT * FROM negocios WHERE nombre_negocio = %s", (nuevo_nombre,))
        existe = cursor.fetchone()

        if existe:
            flash('El nombre de negocio ya existe, prueba con otro.')
            return render_template('asociar_negocio.html', negocios=negocios)

        # Si no existe, inserta
        try:
            cursor.execute("INSERT INTO negocios (nombre_negocio) VALUES (%s)", (nuevo_nombre,))
            conexion.commit()
            flash('Negocio creado exitosamente.')
            return redirect(url_for('dashboard'))  # O donde quieras llevarlo
        except Exception as e:
            flash(f'Error al crear negocio: {e}')
            return render_template('asociar_negocio.html', negocios=negocios)

    return render_template('asociar_negocio.html', negocios=negocios)

@app.route('/dashboard')
def dashboard():
    conexion = conectar_db()  # <-- Aquí te conectas
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    return render_template("dashboard.html", productos=productos)




@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
     nombre = request.form['nombre']
     precio = request.form['precio']
     stock = request.form['stock']
     cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)", (nombre, precio, stock))
     conexion.commit()
     return redirect(url_for('dashboard'))

@app.route('/registrar_venta', methods=['POST'])
def registrar_venta():
    producto = request.form['producto']
    cantidad = int(request.form['cantidad'])
    fecha = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO ventas (producto, cantidad, fecha) VALUES (%s, %s, %s)", (producto, cantidad, fecha))
    conexion.commit()
    return redirect(url_for('dashboard'))

@app.route('/calcular_ganancias', methods=['POST'])
def calcular_ganancias():
     mes_actual = datetime.now().strftime('%Y-%m')
     cursor.execute("SELECT SUM(p.precio * v.cantidad) FROM ventas v JOIN productos p ON v.producto = p.nombre WHERE DATE_FORMAT(v.fecha, '%Y-%m') = %s", (mes_actual,))
     resultado = cursor.fetchone()[0]
     return resultado if resultado else 0
     return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
