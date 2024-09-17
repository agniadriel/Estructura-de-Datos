import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime
from pygame import mixer

name = "maya"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()     
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
        if name in rec:
            rec = rec.replace(name, '')
    except sr.UnknownValueError:
        print("No te entendí, intenta de nuevo")
        rec = ""
    return rec

def run_maya():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No te entendí, intenta de nuevo")
            continue     
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            print("Buscando " + search)
            talk("Buscando " + search)
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)

        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip
            talk("Alarma activada a las " + num + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("DESPIERTA!!!")
                    mixer.init()
                    mixer.music.load("")

        elif 'abre' in rec:
            search = rec.replace('abre', '')
            print("Abriendo " + search)
            talk("Abriendo " + search)
            pywhatkit.search(search)

        elif 'detente' in rec:
            print("Hasta luego")
            talk("Hasta luego")
            break

if __name__ == '__main__':
    run_maya()
