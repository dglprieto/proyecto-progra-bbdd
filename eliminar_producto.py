# eliminar_producto.py

from creacion_engine import Session
from producto import Producto

def eliminar_producto():
    session = Session()

    id_producto = input("Introduce el ID del producto que quieres eliminar: ")
    producto = session.query(Producto).get(id_producto)

    if producto:
        session.delete(producto)
        session.commit()
        print("🗑️ Producto eliminado correctamente.")
    else:
        print("❌ Producto no encontrado.")

    session.close()
