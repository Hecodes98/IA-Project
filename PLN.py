import spacy
import sys
import recognizer as r


class NLP:
    def __init__(self, text):
        self.POS = dict()
        self.STOP = list()
        self.lemma = dict()
        self.entities = list()
        self.text = text  # audio.get_text()
        self.nlp = spacy.load('es')
        self.doc = self.nlp(self.text)

    def getPosDoc(self):
        for token in self.doc:
            if token.pos_ in self.POS:
                self.POS[token.pos_].append([token.text, token.lemma_])
            else:
                self.POS[token.pos_] = []
                self.POS[token.pos_].append([token.text, token.lemma_])
        return self.POS

    def getNoStopToken(self):
        for token in self.doc:
            if token.is_stop:
                self.STOP.append(token)
        return self.STOP
