import PLN as p
import recognizer as r

if __name__ == "__main__":
    mic = r.Recognizer()
    text = mic.get_text()
    print(text)
    pln = p.NLP(text)
    print(pln.getPosDoc())
