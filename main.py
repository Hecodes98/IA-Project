import PLN as p
import recognizer as r
import constants as c
import entities as e
import process_database as pdb
import sys


if __name__ == "__main__":
    mic = r.Recognizer()
    text = "De cual de las regiones esta ubicada risaralda".lower()
    pln = p.NLP(text)
    entities = e.get_entities(text)
    print(entities)
    POS = pln.getPosDoc()
    # print(POS)

    if 'NOUN' in POS:
        nouns = POS['NOUN']
        tables = pdb.getPossibleTable(nouns)
        fields = pdb.get_Possible_Fields(nouns)
        print(tables, entities[0][1], fields)
        print(c.consulta[tables[0]][entities[0][1]][fields[0]])
    else:
        print("No hemos podido procesar tu frase")
