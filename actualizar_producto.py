from creacion_engine import Session
from producto import Producto

def actualizar_producto():
    session = Session()

    id_producto = input("Introduce el ID del producto que quieres actualizar: ")
    producto = session.query(Producto).get(id_producto)

    if producto:
        print(f"Producto actual: {producto.nombre} - {producto.descripcion}")
        nuevo_nombre = input("Introduce el nuevo nombre: ")
        nueva_descripcion = input("Introduce la nueva descripción: ")

        producto.nombre = nuevo_nombre
        producto.descripcion = nueva_descripcion

        session.commit()
        print("✅ Producto actualizado correctamente.")
    else:
        print("❌ Producto no encontrado.")

    session.close()
