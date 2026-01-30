# 🍷 Vinoteca Premium - Sistema de E-Commerce

Sistema completo de tienda online para vinos con panel de administración, desarrollado con **Angular** y **Flask**.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![Angular](https://img.shields.io/badge/Angular-21.0-red?logo=angular)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-38bdf8?logo=tailwindcss)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)

---

## 📋 Índice

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [API REST](#-api-rest)
- [Panel de Administración](#-panel-de-administración)
- [Capturas de Pantalla](#-capturas-de-pantalla)

---

## 🎯 Descripción

**Vinoteca Premium** es una aplicación web full-stack que permite a los usuarios navegar por un catálogo de vinos, añadir productos a un carrito de compras y realizar pedidos. Además, incluye un panel de administración completo para gestionar productos y pedidos.

### 🎨 Diseño

- **Paleta de colores**: Vino (#722F37) y Beige (#F5E6D3)
- **Tipografía**: Playfair Display (títulos) e Inter (texto)
- **Estilo**: Diseño elegante y moderno con glassmorphism y microanimaciones
- **Responsive**: Totalmente adaptable a dispositivos móviles y escritorio

---

## ✨ Características Principales

### 👥 Para Usuarios

- ✅ **Catálogo de Vinos**: Grid responsive con tarjetas elegantes
- ✅ **Vista de Detalles**: Información completa del producto (precio, tipo, añada, grado alcohólico)
- ✅ **Carrito de Compras**: Gestión de productos con persistencia de sesión
- ✅ **Proceso de Pedido**: Formulario validado con datos ficticios
- ✅ **Diseño Premium**: Efectos hover, transiciones suaves, estados vacíos diseñados

### 🔐 Para Administradores

- ✅ **Gestión de Productos**: Crear, editar, eliminar vinos
- ✅ **Gestión de Pedidos**: Visualizar y administrar pedidos de clientes
- ✅ **Autenticación**: Sistema de token para acceso seguro
- ✅ **Interfaz Intuitiva**: Panel de administración con menú de navegación

---

## 🛠️ Tecnologías Utilizadas

### Backend (Python - Flask)

| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Python** | 3.13 | Lenguaje principal del backend |
| **Flask** | 3.0+ | Framework web ligero |
| **Flask-CORS** | Latest | Manejo de peticiones cross-origin |
| **Flask-Session** | Latest | Gestión de sesiones del lado del servidor |
| **SQLite** | 3 | Base de datos embebida |

### Frontend (TypeScript - Angular)

| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Angular** | 21.0 | Framework SPA |
| **TypeScript** | 5.7+ | Lenguaje tipado para desarrollo |
| **TailwindCSS** | 3.0 | Framework CSS utility-first |
| **RxJS** | 7.8+ | Programación reactiva |
| **Bun** | Latest | Runtime y gestor de paquetes JS |

### Herramientas de Desarrollo

- **Git**: Control de versiones
- **VS Code**: Editor de código
- **Chrome DevTools**: Debugging y testing

---

## 🏗️ Arquitectura del Proyecto

```
python_tienda/
├── servidor_python/          # Backend Flask
│   ├── bd/
│   │   ├── conexion.py       # Conexión a SQLite
│   │   └── repositorio_tienda.py  # Operaciones CRUD
│   ├── static/
│   │   ├── imagenes/         # Imágenes de productos
│   │   └── css/             # Estilos para templates Flask
│   ├── templates/           # Templates HTML (Admin)
│   │   ├── index-admin.html
│   │   ├── listar-productos.html
│   │   ├── registrar-vino.html
│   │   ├── listar-pedidos.html
│   │   └── menu.html
│   ├── app_flask.py         # Aplicación principal
│   ├── app_flask_rest.py    # API REST
│   └── app_flask_admin.py   # Panel de administración
│
└── angular_tienda/          # Frontend Angular
    ├── src/
    │   ├── app/
    │   │   ├── vinos/       # Catálogo de productos
    │   │   ├── detalles/    # Vista detalle de producto
    │   │   ├── carrito/     # Carrito de compras
    │   │   ├── pedido/      # Formulario de pedido
    │   │   ├── usuarios/    # Gestión de usuarios
    │   │   ├── model/       # Interfaces TypeScript
    │   │   └── servicio-tienda.ts  # Servicio HTTP
    │   ├── styles.css       # Estilos globales con Tailwind
    │   └── index.html       # HTML principal
    └── tailwind.config.ts   # Configuración Tailwind
```

---

## 📦 Instalación

### Prerrequisitos

- **Python 3.13+** instalado
- **Bun** o **Node.js 18+** instalado
- **Git** (opcional)

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd python_tienda
```

### 2. Configurar Backend (Flask)

```bash
cd servidor_python

# Instalar dependencias
pip install flask flask-cors flask-session

# La base de datos SQLite se creará automáticamente
```

### 3. Configurar Frontend (Angular)

```bash
cd angular_tienda

# Instalar dependencias con Bun
bun install

# O con npm
npm install
```

---

## ⚙️ Configuración

### Backend Flask

Edita `servidor_python/app_flask.py`:

```python
# Puerto del servidor (por defecto 5000)
app.run(port=5000, debug=True)

# Token de administración (cambiar en producción)
ADMIN_TOKEN = "12345"
```

### CORS

El backend está configurado para aceptar peticiones desde:
- `http://localhost:4200` (Angular dev server)

### Base de Datos

La base de datos SQLite se encuentra en:
```
servidor_python/bd/vinoteca.db
```

Tablas principales:
- `vinos`: Productos del catálogo
- `pedidos`: Órdenes de compra
- `pedido_producto`: Relación pedidos-productos

---

## 🚀 Uso

### Iniciar el Backend (Flask)

```bash
cd servidor_python
python app_flask.py
```

El servidor estará disponible en: `http://localhost:5000`

### Iniciar el Frontend (Angular)

```bash
cd angular_tienda
bun start

# O con npm
npm run dev
```

La aplicación estará disponible en: `http://localhost:4200`

### Acceder al Panel de Administración

Desde el navegador, ve a:
```
http://localhost:5000/admin/?token=12345
```

O haz clic en el botón **"Administración"** en el menú de Angular.

---

## 🔌 API REST

Base URL: `http://localhost:5000/rest/`

### Endpoints Principales

#### Productos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/rest/vinos` | Obtener todos los vinos |
| GET | `/rest/obtener_vino_por_id?id={id}` | Obtener vino por ID |

#### Carrito

| Método | Endpoint | Descripción | Requiere Sesión |
|--------|----------|-------------|-----------------|
| POST | `/rest/agregar_producto_a_carrito` | Añadir producto al carrito | ✅ |
| GET | `/rest/obtener_productos_carrito_para_listado` | Obtener productos del carrito con detalles | ✅ |
| GET | `/rest/vaciar_carrito` | Vaciar el carrito | ✅ |

#### Pedidos

| Método | Endpoint | Descripción | Requiere Sesión |
|--------|----------|-------------|-----------------|
| POST | `/rest/registrar_pedido` | Crear nuevo pedido | ✅ |

### Ejemplo de Uso

```javascript
// Agregar producto al carrito
fetch('http://localhost:5000/rest/agregar_producto_a_carrito', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  credentials: 'include', // Importante para sesiones
  body: JSON.stringify({
    id: 1,
    cantidad: 2
  })
});
```

---

## 👨‍💼 Panel de Administración

### Acceso

- **URL**: `http://localhost:5000/admin/?token=12345`
- **Token por defecto**: `12345`

### Funcionalidades

1. **Gestión de Productos**
   - Ver listado completo de vinos
   - Agregar nuevos productos con imagen
   - Editar productos existentes
   - Eliminar productos

2. **Gestión de Pedidos**
   - Ver todos los pedidos
   - Ver detalles de cada pedido
   - Estado y fecha de pedidos

3. **Seguridad**
   - Autenticación basada en token
   - Sesión persistente durante la navegación
   - Botón de cerrar sesión

---

## 📸 Capturas de Pantalla

### Catálogo de Vinos
Grid responsive con tarjetas elegantes mostrando:
- Imagen del producto
- Nombre y precio
- Tipo de vino
- Grado alcohólico y añada
- Botón "Ver Detalles"

### Vista de Detalles
Layout de 2 columnas con:
- Imagen grande a la izquierda
- Información completa y botón "Añadir al Carrito"

### Carrito de Compras
- Lista de productos agregados
- Resumen sticky con total
- Botones "Vaciar" y "Realizar Pedido"

### Panel de Administración
- Menú de navegación con acceso a productos y pedidos
- Tablas con datos completos
- Formularios de edición

---

## 🔐 Seguridad

⚠️ **IMPORTANTE**: Este es un proyecto de demostración. Para producción:

1. ✅ Cambiar `ADMIN_TOKEN` por un sistema de autenticación JWT
2. ✅ Usar variables de entorno para credenciales
3. ✅ Implementar HTTPS
4. ✅ Validar y sanitizar todas las entradas
5. ✅ Usar base de datos PostgreSQL/MySQL en lugar de SQLite
6. ✅ Implementar rate limiting en la API

---

## 🐛 Problemas Conocidos

- El token de admin es estático (usar autenticación real en producción)
- Las imágenes se cargan desde URLs absolutas
- No hay paginación en el catálogo de productos

---

## 🚧 Mejoras Futuras

- [ ] Autenticación de usuarios (registro/login)
- [ ] Pasarela de pago real
- [ ] Sistema de búsqueda y filtros
- [ ] Wishlist/Favoritos
- [ ] Valoraciones y reseñas
- [ ] Historial de pedidos para usuarios
- [ ] Notificaciones por email
- [ ] Panel de estadísticas para admin

---

## 📄 Licencia

Este proyecto es de uso educativo.

---

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje full-stack con Angular y Flask.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Soporte

Para reportar bugs o solicitar features, por favor abre un issue en el repositorio.

---

**¡Disfruta desarrollando con Vinoteca Premium! 🍷**
