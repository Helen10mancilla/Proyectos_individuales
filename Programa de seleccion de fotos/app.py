import os
import shutil
from PIL import Image
from tkinter import filedialog, Tk, Label, Button, Entry, StringVar, Radiobutton, messagebox

def obtener_imagenes(carpeta):
    ext = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    return [os.path.join(carpeta, f) for f in os.listdir(carpeta) if f.lower().endswith(ext)]

def calcular_calidad(imagen_path):
    try:
        img = Image.open(imagen_path)
        ancho, alto = img.size
        return ancho * alto  # hablamos de resolución en píxeles
    except:
        return 0

def seleccionar_mejores(imagenes, cantidad, modo):
    puntuadas = [(img, calcular_calidad(img)) for img in imagenes]
    reverse = (modo == 'alta')
    puntuadas.sort(key=lambda x: x[1], reverse=reverse)
    return puntuadas[:cantidad]

def guardar_en_destino(seleccionadas, carpeta_origen):
    destino = os.path.join(carpeta_origen, 'mejores_fotos')
    os.makedirs(destino, exist_ok=True)
    for img_path, _ in seleccionadas:
        shutil.copy(img_path, os.path.join(destino, os.path.basename(img_path)))
    return destino

def lanzar_gui():
    def seleccionar_y_procesar():
        carpeta = filedialog.askdirectory(title="Selecciona carpeta con fotos")
        if not carpeta:
            messagebox.showwarning("Aviso", "No seleccionaste carpeta.")
            return

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Cantidad inválida.")
            return

        calidad = calidad_var.get()
        imgs = obtener_imagenes(carpeta)
        if not imgs:
            messagebox.showerror("Error", "No hay imágenes.")
            return

        seleccionadas = seleccionar_mejores(imgs, cantidad, calidad)
        carpeta_destino = guardar_en_destino(seleccionadas, carpeta)
        messagebox.showinfo("¡Listo!", f"Fotos guardadas en:\n{carpeta_destino}")

    ventana = Tk()
    ventana.title("Selector de Fotos Simple")
    ventana.geometry("400x250")
    ventana.resizable(False, False)

    Label(ventana, text="¿Cuántas fotos quieres?").pack(pady=10)
    entry_cantidad = Entry(ventana); entry_cantidad.pack()

    Label(ventana, text="Calidad basada en resolución:").pack(pady=10)
    calidad_var = StringVar(value='alta')
    Radiobutton(ventana, text="Alta calidad", variable=calidad_var, value='alta').pack()
    Radiobutton(ventana, text="Baja calidad", variable=calidad_var, value='baja').pack()

    Button(ventana, text="Seleccionar carpeta y procesar", command=seleccionar_y_procesar,
           bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=20)
    ventana.mainloop()

if __name__ == "__main__":
    lanzar_gui()
