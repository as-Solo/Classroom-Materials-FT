import os
import dotenv
from pymongo import MongoClient

<<<<<<< HEAD
print (''' 
-------------------------------------------------------------------------
-------------------------------------------------------------------------
CONFIGURACIÓN EJECUTÁNDOSE
-------------------------------------------------------------------------
-------------------------------------------------------------------------
''')
dotenv.load_dotenv()

# os.getenv('URL')
dburl = "mongodb://localhost/HP"

print(dburl)
if not dburl:
    raise ValueError('No tienes url mongodb')

client = MongoClient(dburl)
db = client.get_database()
collection = db.get_collection("frases")
=======
dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
