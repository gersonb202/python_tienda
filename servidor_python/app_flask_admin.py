# aquí vamo a atender las peticiones para la administración de la tienda
import os
from flask import jsonify, redirect, url_for, request, session, render_template
from __main__ import app
import bd.repositorio_tienda as repo

# aquí irán las rutas de admin
ruta_admin = "/admin/"

@app.route(ruta_admin)
def inicio_admin():
    # Guardar token en sesión si viene en la URL
    token = request.args.get('token')
    if token == ADMIN_TOKEN:
        session['token'] = token
    return render_template("index-admin.html")

# Al igual que con el interceptro en spring boot, en flask podemos proteger la administración:
ADMIN_TOKEN = "12345" # para que sirve?
from functools import wraps
def require_token(f): # Explicar esto
    @wraps(f)
    def funcion_decorada(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            token = request.args.get('token')
        if not token:
            token = session.get('token','')
        if token != ADMIN_TOKEN:
            return "No puedes pasar!"
        return f(*args, **kwargs)
    return funcion_decorada

@app.route(ruta_admin + "logout")
def logout_admin():
    session.pop('token', None)
    return redirect(url_for('inicio_admin'))

@app.route(ruta_admin + "gestionar-productos")
@require_token
def gestionar_productos():
    return render_template("listar-productos.html", vinos = repo.obtener_vinos())

@app.route(ruta_admin + "registrar-vino")
def registrar_vino():
    return render_template("registrar-vino.html")

@app.route(ruta_admin + "guardar-nuevo-vino", methods = ["POST"])
def guardar_nuevo_vino():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    grado = request.form["grado_alcohol"]
    tipo = request.form["tipo"]
    anada = request.form["anada"]
    foto = request.files["foto"]

    id_generada = repo.registrar_vino(nombre, precio, tipo, grado, anada, descripcion)
    # vamos a guardar la foto en static/imgenes/id.jpg
    ruta_proyecto = os.path.dirname(__file__)
    ruta_destino_imagen = \
    os.path.join(ruta_proyecto, "static", "imagenes", str(id_generada) + ".jpg")
    foto.save(ruta_destino_imagen)
    # lo siguiente continua la ejecución en def gestionar_productos() definido más arriba
    return redirect(url_for("gestionar_productos")) # gestionar_productos() # render_template("gestionar_productos")

@app.route(ruta_admin + "gestionar-pedidos")
def gestionar_pedidos():
    pedidos_bd = repo.obtener_pedidos()
    return render_template("listar-pedidos.html", pedidos = pedidos_bd)

@app.route(ruta_admin + "ver-detalles-pedido")
def ver_detalles_pedido():
    id = request.args.get("id")
    pedido_completo = repo.obtener_pedido_completo_por_id(id)
    return render_template("pedido-detalles.html", pedido = pedido_completo)

@app.route(ruta_admin + "borrar-vino/<int:id>")
def borrar_vino(id):
    print(f"Borrar producto de id {id}")
    repo.borrar_vino(id)
    return redirect(url_for("gestionar_productos")) # ojo con esto

@app.route(ruta_admin + "editar-vino/<int:id>")
def editar_vino(id):
    vino_editar = repo.obtener_vino_por_id(id)
    return render_template("editar-vino.html", vino = vino_editar)

@app.post(ruta_admin + "guardar-cambios-vino")
def guardar_cambios_vino():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    grado = request.form["grado_alcohol"]
    tipo = request.form["tipo"]
    anada = request.form["anada"]
    foto = request.files["foto"]
    id = request.form["id"]
    repo.actualizar_vino(nombre, precio, tipo, grado, anada, descripcion, id)
    if request.files["foto"].filename:
        foto = request.files["foto"]
        # pisar la foto anterior
        ruta_proyecto = os.path.dirname(__file__)
        ruta_destino_imagen = \
        os.path.join(ruta_proyecto, "static", "imagenes", str(id) + ".jpg")
        foto.save(ruta_destino_imagen)
    
    return redirect(url_for("gestionar_productos"))