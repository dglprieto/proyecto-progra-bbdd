from catalogo import *
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine
from rich.console import Console
from rich.table import Table

def listar_producto():
    console = Console()
    basedir = os.path.abspath(os.path.dirname(__file__))

    engine = create_engine(
    "sqlite:///" + os.path.join(basedir, 'catalogo.db'),
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    echo=True
    )


    Session = sessionmaker(bind=engine)
    session = Session()

    productos = session.query(Producto).all()
    tabla = Table(title=" LISTA DE PRODUCTOS", show_header=True, header_style="bold blue")
    tabla.add_column("ID", style="cyan", width=10)
    tabla.add_column("Nombre", style="magenta")
    tabla.add_column("Descripción", min_width=20)
    tabla.add_column("Cantidad", justify="right", style="yellow")

    for producto in productos:
        tabla.add_row(
            str(producto.id),
            producto.nombre,
            producto.descripcion,
            str(producto.cantidad)
        )
    console.print(tabla)
