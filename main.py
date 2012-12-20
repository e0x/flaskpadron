#from db import *
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort
from flask_sqlalchemy import SQLAlchemy
import sys


reload(sys)
sys.setdefaultencoding('ISO-8859-1')

app = Flask(__name__)
app.config.from_pyfile('padron.cfg')
db = SQLAlchemy(app)
db.metadata.bind = db.engine

class Padron(db.Model):
	__table__ = db.Table('padron', db.metadata, autoload=True)



@app.route('/')
def index():
    return render_template('show_result.html')


@app.route('/results', methods=['POST'])
def results():
    nombre= request.form['name']
    apellido = request.form['lastname']
    return render_template('show_result.html', personas=Padron.query.filter(Padron.nombre.like(nombre) & Padron.apellido.like(apellido)))



if __name__ == '__main__':
   app.debug = True 
   app.run()

