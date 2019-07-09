import spacy
import sys
import recognizer as r
# Clase encargada del procesamiento del texto dado por el
# usuario para obtener secciones claves de la frase


class NLP:
    def __init__(self, text):
        self.POS = dict()
        self.STOP = list()
        self.lemma = dict()
        self.entities = list()
        self.text = text  # audio.get_text()
        # cargamos el modulo de lenguaje español de la libreria de spacy
        self.nlp = spacy.load('es')
        # se procesa el texto entregando un doc listo para obtener su POS
        self.doc = self.nlp(self.text)

    def getPosDoc(self):  # Aui obtenemos las partes del habla
        for token in self.doc:  # Tokenizamos la frase
            if token.pos_ in self.POS:  # Ingresamos los POS de cada token a un diccionario
                self.POS[token.pos_].append([token.text, token.lemma_])
            else:
                self.POS[token.pos_] = []
                self.POS[token.pos_].append([token.text, token.lemma_])
        return self.POS

    def getNoStopToken(self):  # Obtenemos las palabras de parada
        for token in self.doc:
            if token.is_stop:
                self.STOP.append(token)
        return self.STOP
