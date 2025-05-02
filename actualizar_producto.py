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

        id_producto = int(input("Introduce el ID del producto que quieres actualizar: "))
        producto = session.query(Producto).get(id_producto)

        if producto:
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            nueva_descripcion = input("Introduce la nueva descripción: ")
            nueva_cantidad = int(input("Introduce la nueva cantidad: "))

            producto.nombre = nuevo_nombre
            producto.descripcion = nueva_descripcion
            producto.cantidad = nueva_cantidad

            session.commit()
            print("✅ Producto actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    session.close()
