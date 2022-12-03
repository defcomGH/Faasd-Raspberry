from flask import Flask,render_template
import requests
import time
import db
import random
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse

from forms import SignupForm, PostForm, LoginForm
from models import users, get_user, User

app= Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
login_manager = LoginManager(app)
login_manager.login_view = "login"
posts = []

#Que base de datos ni que base de datos acá hardcodeamos los users y passwords
user = User(len(users) + 1, "Señor x", "Taller", "tdp2")
users.append(user)



# Iniciar base de datos
db.init_app(app)


# JYSERVER
import jyserver.Flask as jsf

## Variables
#urltemp = 'http://192.168.222.202:80/function/temperatura'
#urlhum = 'http://192.168.222.202:80/function/humedad'

"""@jsf.use(app)
class App:
    def __init__(self):
        self.count = -1 #Variable para leer temperatura=0 o humedad=1 o ninguna=-1
        temp = requests.get(urltemp) # Llamar a funcion en rpi con get
        hum = requests.get(urlhum) # Llamar a funcion en rpi con get

    def getTemperatura(self):
        self.count = 0
        contador= 2
        self.js.document.getElementById("DisplayHumedad").style.display='none'      # Hacer no visible el bloque Humedad
        self.js.document.getElementById("DisplayHome").style.display='none'         # Hacer no visible el bloque home
        self.js.document.getElementById("DisplayTemperatura").style.display='block' # Hacer visible el bloque temperatura
        while (self.count==0):                  # Mientras siga en la seccion temperatura
            response = requests.get(urltemp)    # Llamar a funcion en rpi con get y obtener el JSON
            if (str(response)=='<Response [200]>'):
                temp= response.json()
                print(temp)
                db.add_temp(temp['valor'])               # Agregar valor a la base de datos

                self.js.setearTemperatura(temp['valor'])                                               # Actualizar termometro
                if (contador==2):
                    temperaturas= db.ultimosdiez('temperatura')                                         # Obtener valores historicos
                    self.js.actualizarChart(temperaturas,'chartdivTemperatura')                         # Actualizar el grafico
                    self.js.document.getElementById("chartdivTemperatura").style.display='block'        # Hacer visible el grafico
                    contador=0
                else:
                    contador+=1
            else:
                print('Deployeando funcion') 
                
            time.sleep(5)

    def getHumedad(self):
        self.count = 1
        self.js.document.getElementById("DisplayTemperatura").style.display='none'  # Hacer no visible el bloque temperatura
        self.js.document.getElementById("DisplayHome").style.display='none'         # Hacer no visible el bloque home
        self.js.document.getElementById("DisplayHumedad").style.display='block'     # Hacer visible el bloque humedad
        while (self.count==1):                  # Mientras siga en la seccion humedad
            response = requests.get(urlhum)     # Llamar a funcion en rpi con get y obtener el JSON
            if (str(response)=='<Response [200]>'):
                hum= response.json()
                db.add_hum(hum['valor'])                 # Agregar valor a la base de datos

                humedades= db.ultimosdiez('humedad')                                        # Obtener valores historicos
                self.js.actualizarChart(humedades,'chartdivHumedad')                        # Actualizar el grafico
                self.js.setearHumedad(hum['valor'])                                        # Actualizo termometro
                self.js.document.getElementById("chartdivHumedad").style.display='block'    # Hacer visible el grafico
            else:
                print('Deployeando funcion')
                
            time.sleep(5)
  """


@app.route("/")
def default():
    return redirect(url_for('login')) 



@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

#Por si quieren implementar botón de logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Ruta para el Home (usando decorator)
@app.route("/index")
def index():

    #App.count=-1 # Hacer no visible ambos bloques temperatura y humedad
    
    
    if not(current_user.is_authenticated):
        return redirect(url_for('login'))

    data={
        'titulo':'RPI FAASD',
    }
    return render_template('index.html',data=data)

# app.add_url_rule("/", "", temperatura.index, methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
