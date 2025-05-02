#importaciones
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
#declaración clase madre
class Base (DeclarativeBase):
    pass

metadata = Base.metadata
Base = declarative_base()
#declaración tablas
class Producto(Base):
    __tablename__ = 'producto'
    IDPRODUCTO = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    categoria_producto = relationship("Catalogo", back_populates="producto")
class Categoria(Base):
    __tablename__ = 'categoria'
    IDCATEGORIA = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    categoria_producto = relationship("Catalogo",back_populates="categoria" )
class Catalogo(Base):
    __tablename__ = 'catalogo'
    id = Column(Integer, primary_key=True)
    IDPRODUCTO = Column(Integer, ForeignKey('producto.IDPRODUCTO'))
    IDCATEGORIA = Column(Integer, ForeignKey('categoria.IDCATEGORIA'))
    PRECIO = Column(Integer, nullable=False)
    producto = relationship("Producto", back_populates="categoria_producto")
    categoria = relationship("Categoria", back_populates="categoria_producto")