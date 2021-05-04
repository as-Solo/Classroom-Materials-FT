<<<<<<< HEAD
from config.configuration import db, collection

print (''' 
-------------------------------------------------------------------------
-------------------------------------------------------------------------
POSTDATA EJECUTÁNDOSE
-------------------------------------------------------------------------
-------------------------------------------------------------------------
''')

def inserta_mensaje(escena, personaje, frase):

    respuesta = {'scene' : f'{escena}',
                'character_name' : f'{escena}',
                'dialogue' : f'{frase}'
    }

    collection.insert_one(respuesta)
=======
from config.configuration import collection


def insertamensaje(escena,personaje,frase):
    dict_insert = {"scene": escena,
    "character_name": personaje,
    "dialogue": frase 
    }
    collection.insert_one(dict_insert)
    
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
