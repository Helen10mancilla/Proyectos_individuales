<?php
// Conexión directa en cada archivo
$conn = new mysqli("localhost", "root", "", "biblioteca");

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
?>
