from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Categoria(Base):
    __tablename__ = 'categoria'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[Optional[str]] = mapped_column(String(100))

    producto: Mapped[List['Producto']] = relationship('Producto', secondary='producto_categoria', back_populates='categoria')


class Producto(Base):
    __tablename__ = 'producto'

    id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[Optional[str]] = mapped_column(String(100))
    descripcion: Mapped[Optional[str]] = mapped_column(String(200))
    cantidad: Mapped[Optional[int]] = mapped_column(Integer)

    categoria: Mapped[List['Categoria']] = relationship('Categoria', secondary='producto_categoria', back_populates='producto')


t_producto_categoria = Table(
    'producto_categoria', Base.metadata,
    Column('idproducto', ForeignKey('producto.id'), nullable=False),
    Column('idcategoria', ForeignKey('categoria.id'), nullable=False)
)
