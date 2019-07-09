import speech_recognition as sr
# Clase encargada de recibir por microfono la tarea brindada por el usuario


class Recognizer:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def get_text(self):
        with self.mic as source:  # Aqui abrimos un dispositivo de microfono
            # hacemos un procesamiento para eliminar el ruido del ambiente
            self.r.adjust_for_ambient_noise(source)
            print("Say something")
            # obtemeos la frase dada por el usuario
            audio = self.r.listen(source, phrase_time_limit=6)
            print("Time Over")
        try:
            # con la api de google, procesamos todo y lo entregamos en texto
            text = self.r.recognize_google(audio, language='es_CO')
            return text
        except:
            return None
