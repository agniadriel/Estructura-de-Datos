import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Asistente Virtual - Proyecto de Grado")
root.geometry("600x400")  # Tamaño de la ventana

# Cargar las imágenes del personaje
img_normal = Image.open("personaje_normal.png")
img_dj = Image.open("personaje_dj.png")
img_buscar = Image.open("personaje_buscar.png")

# Redimensionar las imágenes para que encajen en la interfaz
img_normal = img_normal.resize((100, 100))
img_dj = img_dj.resize((100, 100))
img_buscar = img_buscar.resize((100, 100))

# Convertir las imágenes a un formato que tkinter pueda usar
img_normal_tk = ImageTk.PhotoImage(img_normal)
img_dj_tk = ImageTk.PhotoImage(img_dj)
img_buscar_tk = ImageTk.PhotoImage(img_buscar)

# Crear un Label para mostrar la imagen del personaje
personaje_label = tk.Label(root, image=img_normal_tk)
personaje_label.place(x=10, y=250)  # Coloca el personaje en la parte inferior izquierda

# Función para mostrar las opciones al hacer clic en el personaje
def mostrar_opciones():
    # Crear botones de opciones en el centro de la ventana
    btn_musica = tk.Button(root, text="Buscar Música", command=cambiar_a_dj)
    btn_buscar = tk.Button(root, text="Buscar", command=cambiar_a_buscar)
    btn_alarma = tk.Button(root, text="Alarma", command=cambiar_a_alarma)
    btn_abrir = tk.Button(root, text="Abrir", command=cambiar_a_abrir)

    btn_musica.place(x=250, y=100)
    btn_buscar.place(x=250, y=150)
    btn_alarma.place(x=250, y=200)
    btn_abrir.place(x=250, y=250)

# Funciones para cambiar la imagen del personaje según la opción seleccionada
def cambiar_a_dj():
    personaje_label.config(image=img_dj_tk)

def cambiar_a_buscar():
    personaje_label.config(image=img_buscar_tk)

def cambiar_a_alarma():
    # Cambiar a una imagen de alarma si la tienes
    personaje_label.config(image=img_normal_tk)

def cambiar_a_abrir():
    # Cambiar a una imagen de abrir si la tienes
    personaje_label.config(image=img_normal_tk)

# Asociar la función de mostrar opciones al clic en el personaje
personaje_label.bind("<Button-1>", lambda e: mostrar_opciones())

# Iniciar el bucle principal de la interfaz
root.mainloop()
