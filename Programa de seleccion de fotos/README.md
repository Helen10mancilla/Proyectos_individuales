#  Bot Selector de Fotos

Este es un bot de escritorio hecho en Python que selecciona automáticamente las **mejores fotos** de una carpeta, basándose en su **resolución (calidad)**. Ideal para elegir las fotos más nítidas antes de subirlas a redes sociales o archivarlas.

---

##  Características

✅ Interfaz gráfica fácil de usar  
✅ Selecciona automáticamente fotos de **alta o baja calidad**  
✅ El usuario elige la **cantidad de fotos** que desea  
✅ Crea una carpeta con las fotos seleccionadas (`mejores_fotos`)  
✅ Funciona **localmente**, sin conexión a internet  
✅ Se puede ejecutar con doble clic (`.exe`) sin necesidad de instalar Python

---

##  Cómo usarlo

###  Opción 1: Ejecutar el `.exe` (sin necesidad de Python)

1. Abre el archivo `bot_fotos.exe`
2. Se abrirá una ventana
3. Selecciona una carpeta con imágenes
4. Ingresa cuántas fotos quieres seleccionar
5. Elige entre **alta** o **baja** calidad
6. ¡Listo! Las fotos se guardarán en una carpeta llamada `mejores_fotos`

---

### Opción 2: Ejecutar con Python (para desarrolladores)

####  Requisitos

- Python 3.11+
- Pillow

bash
-pip install pillow
-ejecutar python app.py

## Estructura del proyecto
 Proyecto
├── bot_fotos_simple.py
├── Ejecutar_Bot_Fotos.bat
├── README.md
└── dist/
    └── app.exe

