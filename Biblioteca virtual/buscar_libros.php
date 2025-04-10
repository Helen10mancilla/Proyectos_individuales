<?php
$conn = new mysqli("localhost", "root", "", "biblioteca");

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Procesar la búsqueda
$busqueda = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $busqueda = $_POST['busqueda'];
}

$sql = "SELECT * FROM libros WHERE titulo LIKE '%$busqueda%' OR autor LIKE '%$busqueda%'";
$result = $conn->query($sql);
?>

<!-- Barra de búsqueda -->
<form method="POST">
    <input type="text" name="busqueda" placeholder="Buscar libros..." value="<?php echo $busqueda; ?>">
    <button type="submit">Buscar</button>
</form>

<!-- Mostrar resultados -->
<?php
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<div>";
        echo "<h2>" . $row['titulo'] . "</h2>";
        echo "<p>Autor: " . $row['autor'] . "</p>";
        echo "<p>Descripción: " . $row['descripcion'] . "</p>";
        echo "</div>";
    }
} else {
    echo "No se encontraron resultados.";
}
?>
