import speech_recognition as sr


class Recognizer:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def get_text(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print("Say something")
            audio = self.r.listen(source, phrase_time_limit=6)
            print("Time Over")
        try:
            text = self.r.recognize_google(audio, language='es_CO')
            return text
        except:
            return None
