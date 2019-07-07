from spacy.pipeline import EntityRuler
import spacy
import constants as c

nlp = spacy.load('es')
ruler = EntityRuler(nlp)

patterns = c.patterns

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)


def get_entities(text):
    texting = ""
    doc = nlp(text.lower()+".")
    ent = [(ent.text.capitalize(), ent.label_) for ent in doc.ents]
    return ent
