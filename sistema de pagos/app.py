from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Crear la base de datos y tabla si no existe
def init_db():
    with sqlite3.connect("pagos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pagos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                monto REAL,
                estado TEXT DEFAULT 'pendiente'
            )
        """)
        # Insertar datos de ejemplo si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM pagos")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO pagos (usuario, monto) VALUES (?, ?)", [
                ("Juan", 100),
                ("Luisa", 150),
                ("Carlos", 200)
            ])
        conn.commit()

@app.route("/")
def index():
    with sqlite3.connect("pagos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pagos")
        pagos = cursor.fetchall()
    return render_template("index.html", pagos=pagos)

@app.route("/pagar/<int:id>")
def pagar(id):
    with sqlite3.connect("pagos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE pagos SET estado = 'pagado' WHERE id = ?", (id,))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
