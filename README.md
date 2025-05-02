# proyecto-progra-bbdd
# Gestor de Productos (SQLite + SQLAlchemy + Rich)

Proyecto de *Programación II – Gestión de Catálogos*  
Autores: *Javier Chavarría* y *Daniela Gutiérrez Liébana*

---

## 📐 Descripción

Aplicación de consola que permite *crear, leer, actualizar y eliminar* productos en una base de datos SQLite mediante SQLAlchemy.  
Las clases ORM (Producto, Categoria, ProductoCategoria) se generaron automáticamente con *sqlacodegen*, cumpliendo el punto extra de la práctica.  
La opción Listar productos formatea la salida usando la librería *Rich*.

---

## 📂 Estructura del proyecto

proyecto-progra-bbdd/
│
├── actualizar_producto.py
├── eliminar_producto.py
├── insertar_producto.py
├── listar_productos.py
│
├── catalogo.py      # modelos generados por sqlacodegen
├── catalogo.db      # base de datos SQLite
│
├── main.py          # menú que invoca las funciones CRUD
├── requirements.txt
└── README.md

---

## 🏗️ Modelo de datos

| Tabla | Columnas |
|-------|----------|
| *producto* | id, nombre, descripcion, cantidad |
| *categoria* | id, nombre |
| *producto_categoria* | idproducto, idcategoria (claves foráneas) |

(Relación muchos-a-muchos producto ↔ categoría.)

---

## ⚙️ Instalación

```bash
# 1 Clona el repo y entra
git clone <URL-del-repo>
cd proyecto-progra-bbdd

# 2 (entorno virtual recomendado)
python3 -m venv .venv
source .venv/bin/activate

# 3 Instala dependencias
pip install -r requirements.txt



⸻

▶️ Uso

python main.py

Menú interactivo:

1. Insertar producto
2. Listar productos   ← tabla Rich
3. Actualizar producto
4. Eliminar producto
5. Salir



⸻

✔️ Requisitos y cumplimiento

Criterio	Estado
CRUD completo operativo	✅
Clases generadas vía sqlacodegen	✅
Almacenamiento en SQLite local	✅
Interfaz de texto con menú	✅
Mejora opcional: Visualización Rich	✅



⸻

📝 Dependencias principales (requirements.txt)

rich>=13.0
SQLAlchemy>=2.0
sqlacodegen>=3.0

(pip freeze > requirements.txt actualizado tras última prueba).

⸻

🖋️ Autores
	•	Javier Chavarría
	•	Daniela Gutiérrez Liébana

Trabajo presentado para la asignatura Programación I– Gestor de Catálogos (Universidad Francisco de Vitoria).