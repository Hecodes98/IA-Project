import PLN as p
import recognizer as r
import constants as c

if __name__ == "__main__":
    mic = r.Recognizer()
    text = 'Cual es la puntuacion de Avatar'
    print(text)
    pln = p.NLP(text)
    POS = pln.getPosDoc()
    print(POS)
    nouns = POS['NOUN']
    tables = ['peliculas']
    for table in c.Tables:
        for synonymous in c.Tables[table]:
            for par in nouns:
                if synonymous in par:
                    tables.append(synonymous)
                    nouns.remove(par)
    print(tables)

    fields = c.Fields[tables[0]]
    for field in fields:
        for synonymous in fields[field]:
            for par in nouns:
                if synonymous in par:
                    print(synonymous)
