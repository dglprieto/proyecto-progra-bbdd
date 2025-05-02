from ddbb.catalogo import *
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

def eliminar_producto():
    basedir = os.path.abspath(os.path.dirname(_file_))

    engine = create_engine(
        "sqlite:///" + os.path.join(basedir, 'catalogo.db'),
        pool_size=5,
        max_overflow=10,
        pool_timeout=30,
        echo=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    id_producto = int(input("Introduce el ID del producto que quieres eliminar: "))
    producto = session.query(Producto).get(id_producto)

    if producto:
        session.delete(producto)
        session.commit()
        print("🗑️ Producto eliminado correctamente.")
    else:
        print("❌ Producto no encontrado.")

    session.close()
