<?php
session_start();
if (!isset($_SESSION['usuario'])) {
    header('Location: login.php');
    exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biblioteca</title>
</head>
<body>
    <h2>Bienvenido, <?php echo $_SESSION['usuario']; ?></h2>
    <a href="logout.php">Cerrar sesión</a>

    <h3>Agregar Libro</h3>
    <form action="guardar_libro.php" method="POST">
        <label for="titulo">Título:</label>
        <input type="text" name="titulo" id="titulo" required>
        <br>
        <label for="autor">Autor:</label>
        <input type="text" name="autor" id="autor" required>
        <br>
        <label for="anio">Año:</label>
        <input type="number" name="anio" id="anio" required>
        <br>
        <label for="genero">Género:</label>
        <input type="text" name="genero" id="genero" required>
        <br>
        <button type="submit">Guardar Libro</button>
    </form>

    <h3>Lista de Libros</h3>
    <ul>
        <?php
        $conexion = new mysqli('localhost', 'root', '', 'biblioteca');
        $resultado = $conexion->query("SELECT * FROM libros");

        while ($libro = $resultado->fetch_assoc()) {
            echo "<li>{$libro['titulo']} - {$libro['autor']} ({$libro['anio']})</li>";
        }

        $conexion->close();
        ?>
    </ul>
</body>
</html>

