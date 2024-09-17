import tkinter as tk
from tkinter import PhotoImage
import speech_recognition as sr
import pyttsx3
import pywhatkit, wikipedia, datetime
from pygame import mixer

 

engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Escuchando...")
            audio = r.listen(source)
            texto = r.recognize_google(audio, language="es-ES")
            print(f"Tú dijiste: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("No se entendió el audio")
            hablar("No se entendió el audio")
        except sr.RequestError:
            print("No se pudo solicitar resultados")
            hablar("No se pudo solicitar resultados")
        return ""

def procesar_comando(event=None):
    comando = escuchar()
    
    if comando:
        if "reproduce" in comando:
            cambiar_imagen(imagen_dj)
            musica = comando.replace('reproduce', '')
            print(f"Reproduciendo {musica}")
            hablar(f"Reproduciendo {musica}")
            pywhatkit.playonyt(musica)
        elif "busca" in comando:
            cambiar_imagen(imagen_estudio)
            busqueda = comando.replace('busca', '')
            wikipedia.set_lang("es")
            print(f"Buscando {busqueda}")
            hablar(f"Buscando {busqueda}")
            resultado = wikipedia.summary(busqueda, sentences=1)
            print(resultado)
            hablar(resultado)
        elif "alarma" in comando:
            cambiar_imagen(imagen_alarma)
            hora = comando.replace('alarma', '').strip()
            hablar(f"Alarma activada a las {hora} horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == hora:
                    print("¡DESPIERTA!")
                    mixer.init()
                    mixer.music.load("")  # Añade tu archivo de sonido
                    mixer.music.play()
                    break
        elif "abre" in comando:
            cambiar_imagen(imagen_normal)
            pagina = comando.replace('abre', '')
            print(f"Abriendo {pagina}")
            hablar(f"Abriendo {pagina}")
            pywhatkit.search(pagina)
        elif "adiós" in comando:
            hablar("Hasta luego")
            ventana.quit()

def cambiar_imagen(nueva_imagen):
    personaje.config(image=nueva_imagen)
    personaje.image = nueva_imagen


ventana = tk.Tk()
ventana.title("Asistente Virtual")
ventana.geometry("600x600")
ventana.config(bg="white")

# Cargar las imágenes del personaje
imagen_normal = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-24-17.21.png")
imagen_dj = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-24-17.25.00-A-2D-ninja-character-sprite-in-a-pixel-art-style_-dressed-as-a-DJ.png")
imagen_estudio = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-25-13.03.png")
imagen_alarma = PhotoImage(file=r"C:\Users\PC\Downloads\DALL·E-2024-08-25-13.02.png")


personaje = tk.Label(ventana, image=imagen_normal, bg="white")
personaje.pack(pady=20)


personaje.bind("<Button-1>", procesar_comando)


ventana.mainloop()
