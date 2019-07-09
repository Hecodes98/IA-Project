import PLN as p
import recognizer as r
import constants as c
import entities as e
import process_database as pdb
import crud as db
import sys
# Función principal encargada de la conexión de todos los módulos


def main():
    mic = r.Recognizer()
    # En esta línea se obtiene el texto bien sea por voz o por texto
    text = "Cuántos departamentos tiene Colombia".lower()
    tokens = text.split(' ')  # tokenizacion del texto
    pln = p.NLP(text)  # Procesamiento del texto
    entities = e.get_entities(text)  # Obtencion de las entidades
    POS = pln.getPosDoc()  # Obtencion de las partes del habla
    no_stop = pln.getNoStopToken()  # Obtencion de las palabras de parada

    if 'ADJ' in POS:
        # Obtencion de todas las posibles palabras candidatas a ser tablas o campos
        for lista in POS['ADJ']:
            POS['NOUN'].append(lista)

    if 'NOUN' in POS:  # Si obtenemos palabras candidatas realizaremos el procesamiento
        nouns = POS['NOUN']
        tables = pdb.get_Possible_Table(nouns)  # Obtencion de posibles tablas
        fields = pdb.get_Possible_Fields(nouns)  # Obtencion de posibles campos
        # Método para saber si es una pregunta especial o no
        special_question = pdb.get_special_question(nouns, entities)
        if not special_question:
            print(fields, entities)
            if fields and entities:
                # Después de realizar todo el procesamiento de la frase, enviamos lo obtenido a una consulta
                db.consulta(entities[0][1], fields[0], tokens)
            else:
                print("No podemos realizar tu consulta")
        else:
            if c.how_many in tokens:
                size = db.depCol()  # Consulta de preguntas especiales
                print("Colombia tiene {} departamentos".format(size))
            else:
                db.depCol()  # Consulta de preguntas especiales
    else:
        print("No hemos podido procesar tu frase")
