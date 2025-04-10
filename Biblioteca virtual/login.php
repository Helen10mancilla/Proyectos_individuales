<?php
// Asegúrate de tener la conexión activa
$conn = new mysqli("localhost", "root", "", "biblioteca");

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Iniciamos la sesión para manejar la autenticación
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Obtenemos los datos del formulario
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);
    
    // Consulta para verificar las credenciales
    $sql = "SELECT * FROM usuarios WHERE email = ? AND password = ?";
    $stmt = $conn->prepare($sql); // Preparamos la consulta
    $stmt->bind_param("ss", $email, $password); // Vinculamos parámetros
    $stmt->execute(); // Ejecutamos la consulta
    $result = $stmt->get_result(); // Obtenemos el resultado

    if ($result->num_rows > 0) {
        // Si las credenciales son correctas, creamos la sesión
        $_SESSION['usuario'] = $email; // Guardamos el email en la sesión
        header('Location: biblioteca.php'); // Redirigimos a la biblioteca
        exit();
    } else {
        // Si las credenciales son incorrectas, mostramos un mensaje
        $error = "Credenciales incorrectas. Por favor, intenta de nuevo.";
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar Sesión</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h1>Iniciar Sesión</h1>
        <?php if (isset($error)): ?>
            <p class="error"><?php echo $error; ?></p>
        <?php endif; ?>
        <form method="POST" action="">
            <label for="email">Correo Electrónico:</label>
            <input type="email" name="email" id="email" required>
            
            <label for="password">Contraseña:</label>
            <input type="password" name="password" id="password" required>
            
            <button type="submit">Ingresar</button>
        </form>
        <p>¿No tienes cuenta? <a href="registro.php">Regístrate aquí</a>.</p>
    </div>
</body>
</html>
