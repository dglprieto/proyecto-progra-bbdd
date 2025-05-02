from ddbb.catalogo import *
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(_file_))

engine = create_engine(
    "sqlite:///" + os.path.join(basedir, 'catalogo.db'),
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    echo=True
)

if _name_ == '_main_':
    Session = sessionmaker(bind=engine)
    session = Session()

    productos = session.query(Producto).all()

    for producto in productos:
        print(f"ID: {producto.id} | Nombre: {producto.nombre} | Descripción: {producto.descripcion} | Cantidad: {producto.cantidad}")

    session.close()