from ddbb.catalogo import *
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

def insertar_producto():
    basedir = os.path.abspath(os.path.dirname(__file__))

    engine = create_engine(
    "sqlite:///" + os.path.join(basedir, 'catalogo.db'),
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    echo=True)

    if __name__== ('__main__'):

        Session = sessionmaker(bind=engine)
        session = Session()
        nombre = input("Introduce el nombre del producto: ")
        descripcion = input("Introduce la descripción del producto: ")
        cantidad = int(input("Introduce la cantidad: "))
        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, cantidad=cantidad)
        session.add(nuevo_producto)
        session.commit()
        print("Producto insertado correctamente.")