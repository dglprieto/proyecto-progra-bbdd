from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base


class Base (DeclarativeBase):
    pass

metadata = Base.metadata
Base = declarative_base()

class ProductoCategoria(Base):
    __tablename__ = 'producto_categoria'

    id = Column(Integer, primary_key=True)
    id_producto = Column(ForeignKey('producto.id_producto'))
    id_categoria = Column(ForeignKey('categoria.id_categoria'))

    producto = relationship('Producto', back_populates='categorias_producto')
    categoria = relationship('Categoria', back_populates='productos_categoria')

class Producto(Base):
    __tablename__ = 'producto'

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(200))

    categorias_producto = relationship('ProductoCategoria', back_populates='producto')

class Categoria(Base):
    __tablename__ = 'categoria'

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))

    productos_categoria = relationship('ProductoCategoria', back_populates='categoria')

t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)
