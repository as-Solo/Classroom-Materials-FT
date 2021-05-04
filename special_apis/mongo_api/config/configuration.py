import os
import dotenv
from pymongo import MongoClient

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