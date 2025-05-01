from producto import *

def insertar_producto():
    session = Session()

    nombre = input("Introduce el nombre del producto: ")
    descripcion = input("Introduce una descripción del producto: ")

    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion)
    session.add(nuevo_producto)
    session.commit()

    print("✅ Producto insertado correctamente.")

    session.close()
