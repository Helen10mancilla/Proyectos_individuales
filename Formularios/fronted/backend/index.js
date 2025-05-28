const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');
const app = express();

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'formulario'
});

app.post('/register', (req, res) => {
  const { nombre, email, password } = req.body;
  const query = 'INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)';
  db.query(query, [nombre, email, password], (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ mensaje: 'Error en el servidor' });
    }
    res.status(200).json({ mensaje: 'Registro exitoso 🚀' });
  });
});
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  // Aquí iría la lógica para verificar usuario
  // Por ejemplo:
  const [result] = await connection.query('SELECT id FROM usuarios WHERE email = ? AND password = ?', [email, password]);

  if (result.length > 0) {
    res.json({ success: true, usuario_id: result[0].id });
  } else {
    res.json({ success: false });
  }
});


app.listen(3001, () => {
  console.log('✅ Servidor backend corriendo en http://localhost:3001');
});
//const cors = require('cors');
//app.use(cors());

