import tkinter as tk
from tkinter import PhotoImage, messagebox
import pyttsx3
import pywhatkit

# Configurar el motor de síntesis de voz
engine = pyttsx3.init()

# Función para hablar
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Opciones seleccionadas
opcion_seleccionada = None

# Función que se activa cuando se selecciona una opción
def seleccionar_opcion(opcion):
    global opcion_seleccionada
    opcion_seleccionada = opcion
    hablar(f"Has seleccionado {opcion}")
    if opcion == "musica":
        label_info.config(text="Escribe el nombre de la canción:")
    elif opcion == "buscar":
        label_info.config(text="Escribe lo que deseas buscar:")
    elif opcion == "alarma":
        label_info.config(text="Configura la alarma (HH:MM):")
    elif opcion == "abre":
        label_info.config(text="Escribe lo que deseas abrir:")
    entry_comando.delete(0, tk.END)

# Función para procesar el comando según la opción seleccionada
def procesar_comando():
    comando = entry_comando.get()
    
    if opcion_seleccionada == "musica":
        hablar(f"Buscando música: {comando}")
        pywhatkit.playonyt(comando)
    elif opcion_seleccionada == "buscar":
        if "ecuador" in comando.lower():
            hablar("Lo siento, no se puede buscar esto. Elige otra opción.")
            messagebox.showinfo("Error", "No se encontró nada relacionado.")
        else:
            hablar(f"Buscando en Wikipedia: {comando}")
            # Aquí agregarías la búsqueda en Wikipedia
    elif opcion_seleccionada == "alarma":
        # Implementar lógica de alarma
        hablar(f"Configurando la alarma a las {comando}")
    elif opcion_seleccionada == "abre":
        hablar(f"Abriendo: {comando}")
        # Implementar lógica para abrir algo
    else:
        hablar("Por favor, selecciona una opción primero.")
    
    # Limpiar el campo de entrada y el texto de la etiqueta de información
    entry_comando.delete(0, tk.END)
    label_info.config(text="Selecciona una opción:")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Asistente Virtual")
ventana.geometry("600x400")
ventana.config(bg="white")

# Cargar las imágenes del personaje
imagen_normal = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-24-17.21.png")
imagen_dj = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-24-17.25.00-A-2D-ninja-character-sprite-in-a-pixel-art-style_-dressed-as-a-DJ.png")
imagen_estudio = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-25-13.03.png")
imagen_alarma = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-25-13.02.png")

# Mostrar el ninja en la esquina inferior izquierda
ninja_label = tk.Label(ventana, image=imagen_normal, bg="white")
ninja_label.place(x=10, y=10)# Posiciona el ninja en la esquina inferior izquierda

ninja_label = tk.Label(ventana, image=imagen_dj, bg="white")
ninja_label.place(x=10, y=1000) 

ninja_label = tk.Label(ventana, image=imagen_estudio, bg="white")
ninja_label.place(x=10, y=10) 

ninja_label = tk.Label(ventana, image=imagen_alarma, bg="white")
ninja_label.place(x=10, y=10) 

# Etiqueta para mostrar información según la opción seleccionada
label_info = tk.Label(ventana, text="Selecciona una opción:", bg="white", font=("Helvetica", 14))
label_info.pack(pady=10)

# Campo de entrada para el comando
entry_comando = tk.Entry(ventana, font=("Helvetica", 14))
entry_comando.pack(pady=10)

# Botón para procesar el comando
boton_procesar = tk.Button(ventana, text="Procesar", font=("Helvetica", 14), command=procesar_comando)
boton_procesar.pack(pady=10)

# Crear botones para las opciones en el centro de la pantalla
frame_opciones = tk.Frame(ventana, bg="white")
frame_opciones.pack(pady=10)

boton_musica = tk.Button(frame_opciones, text="Buscar Música", font=("Helvetica", 12), command=lambda: seleccionar_opcion("musica"))
boton_musica.grid(row=0, column=0, padx=10, pady=5)

boton_buscar = tk.Button(frame_opciones, text="Buscar", font=("Helvetica", 12), command=lambda: seleccionar_opcion("buscar"))
boton_buscar.grid(row=0, column=1, padx=10, pady=5)

boton_alarma = tk.Button(frame_opciones, text="Alarma", font=("Helvetica", 12), command=lambda: seleccionar_opcion("alarma"))
boton_alarma.grid(row=0, column=2, padx=10, pady=5)

boton_abre = tk.Button(frame_opciones, text="Abre", font=("Helvetica", 12), command=lambda: seleccionar_opcion("abre"))
boton_abre.grid(row=0, column=3, padx=10, pady=5)

# Iniciar la interfaz
ventana.mainloop()
