<?php
// Asegúrate de tener la conexión activa
$conn = new mysqli("localhost", "root", "", "biblioteca");

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Procesar el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $titulo = $_POST['titulo'];
    $autor = $_POST['autor'];
    $descripcion = $_POST['descripcion'];
    $usuario_id = $_POST['usuario_id']; // ID del usuario que sube el libro

    // Insertar libro en la base de datos
    $sql = "INSERT INTO libros (titulo, autor, descripcion, usuario_id) VALUES ('$titulo', '$autor', '$descripcion', $usuario_id)";

    if ($conn->query($sql) === TRUE) {
        echo "Libro subido exitosamente.";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<!-- Formulario para subir libros -->
<form method="POST">
    <label>Título del libro:</label>
    <input type="text" name="titulo" required>
    <label>Autor:</label>
    <input type="text" name="autor" required>
    <label>Descripción:</label>
    <textarea name="descripcion" required></textarea>
    <label>ID de Usuario:</label> <!-- Este campo puede llenarse automáticamente si usas sesiones -->
    <input type="number" name="usuario_id" required>
    <button type="submit">Subir Libro</button>
</form>
