from flask import Flask
from flask_session import Session
from flask_cors import CORS

app = Flask(__name__)
# Habilitar CORS para permitir peticiones desde Angular con credenciales
CORS(app, 
     origins=["http://localhost:4200"],
     supports_credentials=True)
# En flask hay que hacer lo siguiente para poder usar la session
app.secret_key = "1234"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

import app_flask_rest
import app_flask_admin

@app.route("/")
def inicio():
    return "servidor de python operativo"

app.config["DEBUG"] = True
app.run()

# /rest/obtener_productos_carrito
# localhost/server/vinos