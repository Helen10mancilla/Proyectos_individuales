<?php
session_start();
if (!isset($_SESSION['usuario'])) {
    header('Location: login.php');
    exit();
}

$conexion = new mysqli('localhost', 'root', '', 'biblioteca');

if ($conexion->connect_error) {
    die('Error de conexión: ' . $conexion->connect_error);
}

$titulo = $_POST['titulo'];
$autor = $_POST['autor'];
$anio = $_POST['anio'];
$genero = $_POST['genero'];

$query = $conexion->prepare("INSERT INTO libros (titulo, autor, anio, genero) VALUES (?, ?, ?, ?)");
$query->bind_param('ssis', $titulo, $autor, $anio, $genero);

if ($query->execute()) {
    header('Location: biblioteca.php');
} else {
    echo "Error al guardar el libro. <a href='biblioteca.php'>Volver</a>";
}

$query->close();
$conexion->close();
?>
