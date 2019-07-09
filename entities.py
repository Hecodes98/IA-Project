from spacy.pipeline import EntityRuler
import spacy
import constants as c
# Seccion encargada de obtener las entidades implicadas en la frase

nlp = spacy.load('es')  # cargamos el modulo de español
ruler = EntityRuler(nlp)

patterns = c.patterns

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)


def get_entities(text):  # Función encargada de la obtención de las entidades
    doc = nlp(text.lower()+".")
    ent = [(ent.text.capitalize(), ent.label_) for ent in doc.ents]
    return ent
