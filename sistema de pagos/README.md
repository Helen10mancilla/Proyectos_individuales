# 💸 Sistema de Pagos Automático con Flask

Este es un proyecto sencillo hecho en Python con Flask que simula un sistema de pagos. Permite registrar pagos y actualizar su estado automáticamente de **"pendiente"** a **"pagado"** desde una interfaz web.

---

##  Características

- Listado de pagos con nombre de usuario, monto y estado.
- Botón para marcar pagos como "pagado".
- Estado visual: verde para pagados, rojo para pendientes.
- Base de datos local con SQLite (simulación).
- Código claro y fácil de entender, ideal para aprender Flask.

---

##  Tecnologías usadas

- Python  
- Flask 
- SQLite (base de datos local para pruebas) 
- HTML + CSS 

> **Nota:** El sistema actualmente utiliza SQLite como base de datos local para simular registros de pagos. Sin embargo, puede ser fácilmente adaptado para trabajar con bases de datos reales (como MySQL o PostgreSQL) y conectarse a **pasarelas de pago reales** como **Stripe, PayPal o MercadoPago**.  
>  
> Esta funcionalidad está pensada para futuras versiones.

---

##  Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Helen10mancilla/Proyectos_individuales.git
   cd sistema de pagos
   ```

2. Instala las dependencias:
   ```bash
   pip install flask
   ```

3. Ejecuta el servidor:
   ```bash
   python app.py
   ```

4. Abre el navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##  Estructura del proyecto

```
mi_sistema_pagos/
│
├── app.py               # Backend con Flask
├── pagos.db             # Base de datos SQLite (se genera automáticamente)
├── templates/
│   └── index.html       # Interfaz web
└── README.md            # Este archivo
```

---



## Futuras mejoras

- Conexión con pasarelas de pago reales (Stripe, PayPal, MercadoPago).
- Autenticación de usuarios (login/registro).
- Panel de administración con control de pagos.
- Exportación de reportes (PDF, Excel).
- Sistema de notificaciones por correo o WhatsApp.

---



