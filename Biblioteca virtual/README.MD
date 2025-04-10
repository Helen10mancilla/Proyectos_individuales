#  Biblioteca Virtual

Este proyecto consiste en una plataforma web que permite leer y subir libros, conectándose a una base de datos MySQL para almacenar y gestionar la información. Fue desarrollada en PHP y puede ser utilizada como base para sistemas de gestión bibliotecaria.

##  Tecnologías utilizadas

- PHP – Lógica del lado del servidor
- MySQL – Base de datos para almacenar libros, usuarios y metadatos
- CSS – Estilos para lainterfaz web


##  Funciones principales

- 📥 Subida de libros en formato PDF (o el que uses)
- 📖 Lectura en línea de libros desde la plataforma
- 🔐 Gestión de usuarios (login/registro)
- 🔎 Búsqueda y listado de libros disponibles

##  Requisitos

- Servidor local como XAMPP
- PHP 
- MySQL 

##  Instalación y uso

1. Clona este repositorio o copia los archivos en la carpeta `htdocs` de XAMPP (o el equivalente en tu servidor).
2. Crea una base de datos en phpMyAdmin llamada,  `biblioteca`.
3. Configurá la conexión a la base de datos en el archivo PHP correspondiente (ejemplo `conexion.php`):

```php
$conexion = new mysqli("localhost", "root", "", "biblioteca");
