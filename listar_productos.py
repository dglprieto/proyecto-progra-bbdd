from creacion_engine import Session
from producto import Producto

def listar_productos():
    session = Session()

    productos = session.query(Producto).all()

    if productos:
        print("LISTADO DE PRODUCTOS:")
        for producto in productos:
            print(f"ID: {producto.id} | Nombre: {producto.nombre} | Descripción: {producto.descripcion}")
    else:
        print("No hay productos registrados.")

    session.close()