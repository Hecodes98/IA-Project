from pymongo import MongoClient
import constants as c

mc = MongoClient(
    "mongodb+srv://karem-admin:karemgiovanna10@clusterinicial-qrqbw.mongodb.net/test?retryWrites=true&w=majority")

db = mc.ia
collection = db.departamentos


def depCol():  # Función encargada de realizar consultas especiales
    # Aqui se realiza la consula
    query = collection.find({}, {"nombreDepto": 1, "_id": 0})
    size = 0
    for i in query:
        size += 1
        print(i)
    return size


def consulta(nombre, field, token):  # Función encargada de realizar la solicitud a la base de datos
    query = collection.find({"nombreDepto": nombre}, {field: 1, "_id": 0})
    size = 0
    for i in query:
        print(i)
    if c.how_many in token:
        key = list(i.keys())[0]
        print(nombre + " tiene " + str(len(i[key])))


# def cuantosMun(nombre):
#     x = 0
#     query = collection.find({"nombreDepto": nombre}, {
#         "municipioDepto": 1, "_id": 0})
#     for i in query:
#         x = len(i["municipioDepto"])
#     print(x)


# def numDepReg(region):
#     x = 0
#     query = collection.count_documents({"regionDepto": region})
#     print(query)


# if __name__ == "__main__":
#     depCol()
#     munDep(nombre)
#     consulta(nombre, field)
#     cuantosMun(nombre)
# #     numDepReg(region)
