import spacy
import sys
import recognizer as r


class NLP:
    def __init__(self, text):
        self.POS = {}
        self.text = text  # audio.get_text()
        self.nlp = spacy.load('es')
        self.doc = self.nlp(self.text)

    def getPosDoc(self):
        for token in self.doc:
            print("Token {}, POS {}, dependencia {}, principal {} head.pos_ {} ".format(
                token.text, token.pos_, token.dep_, token.head.text, token.head.pos_))
        for token in self.doc:
            if token.pos_ in self.POS:
                self.POS[token.pos_].append(token.text)
            else:
                self.POS[token.pos_] = []
                self.POS[token.pos_].append(token.text)
        return self.POS

    def getPredominantNoun(self):
        for token in self.doc:
            if token.text == token.head.text:
                return token.text


# nouns = []
# POS = {}

# audio = r.Recognizer()
# nlp = spacy.load('es')
# text = audio.get_text()
# doc = nlp(text)


# def getPOSdoc(doc):
#     global POS
#     for token in doc:
#         if token.pos_ in POS:
#             POS[token.pos_].append(token.text)
#         else:
#             POS[token.pos_] = []
#             POS[token.pos_].append(token.text)


# getPOSdoc(doc)


# def getPredominantNoun(doc):
#     for token in doc:
#         if token.text == token.head.text:
#             return token.text


# for token in doc:
#     print("Token {}, POS {}, dependencia {}, principal {}".format(
#         token.text, token.pos_, token.dep_, token.head.text))


# print(POS)
# table = getPredominantNoun(doc)


# for chunk in doc.noun_chunks:
#     print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
