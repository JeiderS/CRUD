from pymongo import MongoClient
import certifi
MONGO_URI = 'mongodb+srv://marcomontes2112:1002134049@cluster0.zgvbbxb.mongodb.net/'

ca = certifi.where()

# definimos el método de conexión
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_baseD_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db