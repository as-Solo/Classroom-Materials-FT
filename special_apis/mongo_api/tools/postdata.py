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