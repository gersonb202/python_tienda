# Aquí vamos a mapear todas las peticiones tipo rest
from flask import jsonify, request, session
from __main__ import app
import bd.repositorio_tienda as repo

# aquí irán las rutas de los servicios REST
ruta_servicios_rest = "/rest/"

@app.get(ruta_servicios_rest)
def inicio_servicio_rest():
    return "servicios REST operativos"

@app.get(ruta_servicios_rest + "vinos")
def obtener_vinos():
    return jsonify(repo.obtener_vinos())

@app.get(ruta_servicios_rest + "usuarios")
def obtener_usuarios():
    return jsonify(repo.obtener_usuarios())

@app.get(ruta_servicios_rest + "obtener_vino_por_id")
def obtener_vino_por_id():
    id = request.args.get("id")
    print(f"buscar registro de id: {id}")
    return jsonify(repo.obtener_vino_por_id(int(id)))

@app.post(ruta_servicios_rest + "agregar_producto_a_carrito")
def agregar_producto_a_carrito():
    id = request.get_json()["id"]
    cantidad = request.get_json()["cantidad"]

    if "carrito" not in session:
        session["carrito"] = []


    productos = session["carrito"]
    encontrado = False
    # Buscar el producto en el carrito
    # si lo encuentro, incremento su cantidad
    for p in productos:
        if p["id"] == id:
            encontrado = True
            p["cantidad"] += cantidad
            break

    # si no lo encuentro, pues loi meto en el carrito
    if not encontrado:
        productos.append({
            "id": id,
            "cantidad": cantidad
        })
    session["carrito"] = productos
    return jsonify("ok")

@app.get(ruta_servicios_rest + "obtener_productos_carrito")
def obtener_productos_carrito():
    if "carrito" not in session:
        session["carrito"] = []
    return jsonify(session["carrito"])

@app.get(ruta_servicios_rest + "obtener_productos_carrito_para_listado")
def obtener_productos_carrito_para_listado():
    if "carrito" not in session or not session["carrito"]:
        session["carrito"] = []
        return jsonify([])
    
    session["carrito"] = sorted(session["carrito"], key=lambda p: p["id"])
    productos_carrito_listado = repo.obtener_productos_carrito_listado(session["carrito"])
    # Lo anterior no incluye la cantidad del producto, vamos a agregarselo
    respuesta = []
    for i,p in enumerate(session["carrito"]):
        respuesta.append({
            "vino": productos_carrito_listado[i],
            "cantidad": p["cantidad"]
        })
    return jsonify(respuesta)

@app.get(ruta_servicios_rest + "vaciar_carrito")
def vaciar_carrito():
    #session.clear() #esto eliminaria todo lo que hay en sesion
    session["carrito"] = []
    return jsonify("carrito vaciado correctamente")

@app.post(ruta_servicios_rest + "registrar_pedido")
def registrar_pedido():
    import re
    
    # Verificar que el carrito no esté vacío
    if "carrito" not in session or not session["carrito"]:
        return jsonify({"error": "El carrito está vacío. Agrega productos antes de realizar un pedido."})

    nombre = request.get_json().get("nombre","")
    if not re.match(r"^[a-zA-Z áéíóúÁÉÍÓÚñÑ\s]{3,50}$", nombre):
        return jsonify({"error":"Nombre no es válido (debe tener entre 3 y 50 caracteres)"})

    numeroTarjeta = request.get_json().get("numeroTarjeta","")
    if not re.match(r"^[0-9]{13,19}$", numeroTarjeta):
        return jsonify({"error":"Número de tarjeta no es válido (debe tener entre 13 y 19 dígitos)"})

    direccion = request.get_json().get("direccion", "")
    if not direccion or len(direccion) < 5:
        return jsonify({"error":"Dirección no es válida (debe tener al menos 5 caracteres)"})

    ip_usuario = request.remote_addr
    user_agent = request.headers.get("User-Agent")

    print(f"registrar pedido de {nombre}, tarjeta: {numeroTarjeta}, direccion: {direccion}, ip: {ip_usuario}, navegador: {user_agent}")

    repo.registrar_pedido(nombre, numeroTarjeta, direccion, session["carrito"])
    session["carrito"] = []
    return jsonify("ok")