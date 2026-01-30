# Preparar una conexión con SQLite
import sqlite3
import shutil
from pathlib import Path
import os
def crear_conexion():

    conexion = sqlite3.connect("bd_tienda_vinos.db")

    # Preparar las tablas iniciales
    # Preparar una conexión con SQLite
    cursor = conexion.cursor()  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vinos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            tipo TEXT NOT NULL,
            grado_alcohol REAL NOT NULL,
            anada INTEGER NOT NULL,
            descripcion TEXT,
            activo INTEGER,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabla de Pedidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo TEXT NOT NULL,
            direccion TEXT NOT NULL,
            numero_tarjeta TEXT NOT NULL,
            fecha TEXT NOT NULL DEFAULT (datetime('now')),
            estado TEXT NOT NULL DEFAULT 'pendiente'
        )
    ''')

    # Tabla de Detalles del Pedido
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedido_producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            vino_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
            FOREIGN KEY (vino_id) REFERENCES vinos(id)
        )
    ''')

    # Crear índices
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_pedido_producto ON pedido_producto(pedido_id)')


    # Preparar unos registros inicialesm si las tablas están vacías
    cursor.execute("SELECT COUNT(*) FROM vinos")
    if cursor.fetchone()[0] == 0:
      
        cursor.executescript("""
        INSERT INTO vinos (nombre, precio, tipo, grado_alcohol, anada, descripcion, activo) VALUES
        ('Rioja Reserva Premium', 25.50, 'Tinto', 14.5, 2018, 'Vino tinto con cuerpo, envejecido en barrica de roble', 1),
        ('Albariño Gallego', 18.75, 'Blanco', 12.0, 2022, 'Vino blanco fresco y aromático de Galicia', 1),
        ('Cava Brut Nature', 12.99, 'Espumoso', 11.5, 2021, 'Espumoso elegante y burbujeante', 1),
        ('Tempranillo Joven', 14.20, 'Tinto', 13.8, 2023, 'Vino joven con frutas rojas y especias', 1),
        ('Verdejo de Rueda', 16.50, 'Blanco', 12.5, 2022, 'Blanco seco con mineralidad y frescura', 1),
        ('Rosado de Provence', 13.45, 'Rosado', 12.2, 2023, 'Rosado ligero con notas de fresas', 1),
        ('Garnacha Vieja Viña', 22.30, 'Tinto', 15.0, 2019, 'Tinto potente con taninos maduros', 1),
        ('Sauvignon Blanc', 17.80, 'Blanco', 13.0, 2022, 'Blanco con notas herbáceas y cítricas', 1),
        ('Cabernet Sauvignon', 28.60, 'Tinto', 14.8, 2017, 'Tinto de guarda con estructura compleja', 1),
        ('Moscatel Dulce', 15.40, 'Dulce', 15.5, 2020, 'Vino dulce con notas de uva moscatel', 1),
        ('Merlot Suave', 19.25, 'Tinto', 13.5, 2021, 'Tinto suave y afrutado de buen beber', 1),
        ('Pinot Grigio', 14.80, 'Blanco', 12.3, 2023, 'Blanco italiano ligero y refrescante', 1),
        ('Tinto Reserva Especial', 35.75, 'Tinto', 14.2, 2016, 'Vino de colección con envejecimiento prolongado', 1),
        ('Champagne Brut', 45.99, 'Espumoso', 12.0, 2019, 'Champagne francés de denominación de origen', 1),
        ('Vino Tinto Joven Ecológico', 11.50, 'Tinto', 12.8, 2023, 'Tinto ecológico sin sulfitos añadidos', 1),
        ('Blanco Aromático Premium', 21.65, 'Blanco', 13.2, 2022, 'Blanco con aromas complejos y persistentes', 1),
        ('Rosado Espumoso', 16.90, 'Rosado', 11.8, 2023, 'Rosado burbujeante y festivo', 1),
        ('Syrah Intenso', 24.40, 'Tinto', 14.6, 2020, 'Tinto con notas de frutas negras y pimienta', 1),
        ('Riesling Alemán', 19.80, 'Blanco', 11.5, 2021, 'Blanco alemán con equilibrio dulce-ácido', 1),
        ('Vino de Mesa Tinto Tradicional', 9.99, 'Tinto', 12.0, 2023, 'Tinto clásico y asequible para el día a día', 1)
        """)
        # copiar imágenes de imagenes_iniciales a static/imagenes
        print("Copiando imágenes iniciales...")
        try:
            base_dir = Path(__file__).resolve().parents[1]  # proyecto/servidor_python
            src_dir = base_dir / "static" / "imagenes" / "imagenes_iniciales"
            dest_dir = base_dir / "static" / "imagenes"
            print(f"Directorio origen: {src_dir}")
            print(f"Directorio destino: {dest_dir}")
            if src_dir.exists() and src_dir.is_dir():
                dest_dir.mkdir(parents=True, exist_ok=True)
                for item in src_dir.iterdir():
                    if item.is_file():
                        shutil.copy2(item, dest_dir / item.name)
        except Exception as e:
            print(f"Error copiando imágenes iniciales: {e}")

        # source_dir = "../static/imagenes/imagenes_iniciales"
        # dest_dir = "../static/imagenes"

        # if os.path.exists(source_dir):
        #     os.makedirs(dest_dir, exist_ok=True)
        #     for filename in os.listdir(source_dir):
        #         src_file = os.path.join(source_dir, filename)
        #         if os.path.isfile(src_file):
        #             shutil.copy(src_file, dest_dir)

        # Insertar datos de ejemplo en la tabla pedidos
        cursor.executescript("""
        INSERT INTO pedidos (nombre_completo, direccion, numero_tarjeta, estado) VALUES
        ('Juan Pérez García', 'calle maldonado, 2', '1111 222', 'completado'),
        ('María López Fernández', 'el kiosko de la esquina, 10', '2222 3333', 'pendiente'),
        ('Juan Pérez García', 'la esquina, 20', '3333 4444', 'enviado'),
        ('Carlos Martínez Ruiz', 'al lado, 5', '5555 666', 'completado'),
        ('María López Fernández', 'donde no se llega, 29', '1010 2020', 'pendiente')
        """) 

        # Insertar datos de ejemplo en la tabla pedido_producto
        cursor.executescript("""
        INSERT INTO pedido_producto (pedido_id, vino_id, cantidad) VALUES
        (1, 1, 2),
        (1, 5, 3),
        (2, 3, 1),
        (2, 8, 2),
        (3, 9, 3),
        (3, 13, 2),
        (4, 14, 1),
        (5, 7, 2),
        (5, 11, 3),
        (5, 18, 2)
        """)
        conexion.commit()
    #conexion.close()
    print("--------- conexión ok -------------")
    return conexion