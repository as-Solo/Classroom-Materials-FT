from flask import Flask, request
<<<<<<< HEAD


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola mundo'



@app.route('/ejemplo_01')
def prueba():
    return 'prueba_01'


@app.route('/ejemplo_02')
def prueba_02():
    return 'Esto no me lo esperaba'
=======
import tools.datos as dat
from  tools.paraeldado import funciondado




app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"


@app.route("/fer")
def datos():
    fer = dat.datosFer()
    return fer


@app.route("/ana")
def datos2():
    ana = dat.datosAna()
    return ana


@app.route("/tiraeldado")
def dado():
    return funciondado()



>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f





<<<<<<< HEAD
app.run("0.0.0.0", 5000, debug = True)
=======
app.run("0.0.0.0",5000, debug=True)
 
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
