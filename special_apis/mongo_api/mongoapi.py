from flask import Flask, request
import tools.getdata as get
import tools.postdata as post
import json
from flask import jsonify
import markdown.extensions.fenced_code

#json.encode(analytics, cls=JSONEncoder)

app = Flask(__name__)



@app.route('/')
def index():
    readme_file = open('Readme.md', 'r')
    ms_template = markdown.markdown(readme.file.read(), extensions = ['fenced_code'])



@app.route("/frases")
def frases():
    frases = get.mensaje_personaje()
    #print (frases)
    return jsonify(frases)


@app.route("/frases/<name>")
def frases_p(name):
    frases = get.mensaje_personajes(name)
    #print (frases)
    return jsonify(frases)


# De normal, flask entiende que por defecto el método es Get, pero si queremos hacer un 'formulario' tenemos que definir el método como POST
@app.route('/nuevafrase', methods = ['POST'])
def insertmensaje():
    escena = request.form.get('scene')
    personajes = request.form.get('character_name')
    frase = request.form.get('dialogue')
    post.inserta_mensaje(escena, personaje, frase)
    return 'Gracias por tu frase, ya eres libre.'







app.run('localhost', '5000', debug = True)