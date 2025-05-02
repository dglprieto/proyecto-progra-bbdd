from sqlalchemy.orm import sessionmaker
from ddbb.creacion_engine import engine
from ddbb.catalogo import Producto

Session = sessionmaker(bind=engine)
session = Session()

    nombre = input("Introduce el nombre del producto: ")
    descripcion = input("Introduce una descripción del producto: ")
    cantidad = int(input("Introduce la cantidad del producto: "))

    nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, cantidad=cantidad)
    session.add(nuevo_producto)
    session.commit()

    print("✅ Producto insertado correctamente.")

    session.close()
