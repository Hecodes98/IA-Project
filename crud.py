from pymongo import MongoClient

mc = MongoClient("mongodb+srv://karem-admin:karemgiovanna10@clusterinicial-qrqbw.mongodb.net/test?retryWrites=true&w=majority")

db = mc.ia
collection = db.departamentos

field = "regionDepto"
nombre = "Risaralda"
region = "Andina"

def depCol():
    query = collection.find({},{"nombreDepto":1 , "_id": 0})
    for i in query:
        print(i)

def munDep(nombre):
    query = collection.find({"nombreDepto" : nombre}, {"municipioDepto":1, "_id":0})
    for i in query:
        print(i)

def consulta(nombre,field):
    query = collection.find({"nombreDepto" : nombre}, {field:1, "_id":0})
    for i in query:
        print(i)

def cuantosMun(nombre):
    x = 0;
    query = collection.find({"nombreDepto": nombre}, {"municipioDepto":1, "_id":0})
    for i in query:
        x = len(i["municipioDepto"])
    print(x)

def numDepReg(region):
    x = 0;
    query = collection.count_documents({"regionDepto": region})
    print(query)



if __name__ == "__main__":
    depCol()
    munDep(nombre)
    consulta(nombre,field)
    cuantosMun(nombre)
    numDepReg(region)
