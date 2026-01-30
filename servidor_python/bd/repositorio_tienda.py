# Aquí vamos a centralizar las operaciones con BD de la tienda
import bd.conexion as conexion
import os

def obtener_vinos( where_sql = ""):
    conn = conexion.crear_conexion()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM vinos {where_sql}")
    filas = cursor.fetchall()
    
    # Convertir a lista de diccionarios
    vinos = []
    for fila in filas:
        vino = {
            'id': fila[0],
            'nombre': fila[1],
            'precio': fila[2],
            'tipo': fila[3],
            'grado_alcohol': fila[4],
            'anada': fila[5],
            'descripcion': fila[6],
            'fecha_creacion': fila[7]
        }
        vinos.append(vino)
    cursor.close()
    conn.close()
    return vinos

def obtener_vino_por_id(id):
    conn = conexion.crear_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vinos WHERE id = ?", (id,))
    fila = cursor.fetchone()
    
    if fila:
        vino = {
            'id': fila[0],
            'nombre': fila[1],
            'precio': fila[2],
            'tipo': fila[3],
            'grado_alcohol': fila[4],
            'anada': fila[5],
            'descripcion': fila[6],
            'fecha_creacion': fila[7]
        }
        conn.close()
        return vino
    cursor.close()
    conn.close()
    return None

def obtener_productos_carrito_listado(productos_session):
    # Vamos a lanzar una consulta en bd por cada id en productos_session
    ids_sql = []
    # los productos agregados a sesion,no tienen por qué estar en orden
    # para ordenarlos por id:

    for p in productos_session:
        ids_sql.append(str(p["id"]))

    ids_consulta = ",".join(ids_sql) # Esta operación forma una string con todos los elementos de ids_sql metiendo una coma entre cada uno de ellos
    where_sql = f"WHERE id IN ({ids_consulta}) ORDER BY id ASC"
    vinos = obtener_vinos(where_sql)
    return vinos

def registrar_vino(nombre, precio, tipo, grado, anada, descripcion):
    conn = conexion.crear_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vinos (nombre, precio, tipo, grado_alcohol, anada, descripcion) VALUES (?, ?, ?, ?, ?, ?)",
        (nombre, precio, tipo, grado, anada, descripcion)
    )
    conn.commit()
    cursor.close()
    conn.close()

def registrar_pedido(nombre, numeroTarjeta, direccion, productos_pedido):
    conn = conexion.crear_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO pedidos (nombre_completo, direccion, numero_tarjeta) VALUES (?, ?, ?)"
    cursor.execute(sql, (nombre, direccion, numeroTarjeta))
    conn.commit()
    id_pedido = cursor.lastrowid
    # registramos en la tabla pedido_producto los productos del pedido registrado
    for pc in productos_pedido:
        id_producto = pc["id"]
        cantidad = pc["cantidad"]
        sql = "INSERT INTO pedido_producto (pedido_id, vino_id, cantidad) VALUES (?, ?, ?)"
        cursor.execute(sql, (id_pedido, id_producto, cantidad))
    conn.commit()
    cursor.close()
    conn.close()
    return id_pedido

def obtener_pedidos():
    conn = conexion.crear_conexion()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM pedidos")
    filas = cursor.fetchall()
    
    # Convertir a lista de diccionarios
    pedidos = []
    for fila in filas:
        pedido = {
            'id': fila[0],
            'nombre_completo': fila[1],
            'direccion': fila[2],
            'numero_tarjeta': fila[3],
            'fecha': fila[4],
            'estado': fila[5]
        }
        pedidos.append(pedido)
    cursor.close()
    conn.close()
    return pedidos

def obtener_pedido_completo_por_id(id):
    conn = conexion.crear_conexion()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT id, nombre_completo, direccion, numero_tarjeta, fecha, estado FROM pedidos WHERE id = ?",
            (id,)
        )
        row = cur.fetchone()
        if row is None:
            return None
        cols = [c[0] for c in cur.description]
        pedido = dict(zip(cols, row))

        cur.execute(
            "SELECT pp.vino_id AS vino_id, v.nombre, v.tipo, v.precio, pp.cantidad "
            "FROM pedido_producto pp "
            "LEFT JOIN vinos v ON v.id = pp.vino_id "
            "WHERE pp.pedido_id = ?",
            (id,)
        )
        prod_cols = [c[0] for c in cur.description]
        prod_rows = cur.fetchall()
        pedido["productos"] = [dict(zip(prod_cols, r)) for r in prod_rows]

        return pedido
    finally:
        cur.close()
        conn.close()

def borrar_vino(id):
    conn = conexion.crear_conexion()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM vinos WHERE id = ?", (id,)
        )
    conn.commit()
    cur.close()
    conn.close()
    #borrar el archivo asociado
    ruta_imagen = f"static/imagenes/{id}.jpg"
    if os.path.exists(ruta_imagen):
        os.remove(ruta_imagen)

def actualizar_vino(nombre, precio, tipo, grado, anada, descripcion, id):
    conn = conexion.crear_conexion()
    cur = conn.cursor()
    cur.execute(
        "UPDATE vinos SET nombre = ?, precio = ?, tipo = ?, grado_alcohol = ?, anada = ?, descripcion = ? WHERE id = ? ",
        (nombre, precio, tipo, grado, anada, descripcion, id)
        )
    conn.commit()
    cur.close()
    conn.close()