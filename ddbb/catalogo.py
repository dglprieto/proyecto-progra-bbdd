from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

class Base (DeclarativeBase):
    pass
metadata = Base.metadata


class RecetaIngrediente(Base):
    __tablename__ = 'receta_ingrediente'

    id = Column(Integer, primary_key=True)
    IDINGREDIENTE = Column(ForeignKey('ingrediente.IDINGREDIENTE'))
    IDRECETA = Column(ForeignKey('receta.IDRECETA'))
    CANTIDAD = Column(Integer, nullable=False)

    ingrediente = relationship('Ingrediente')
    receta = relationship('Receta')
class Ingrediente(Base):
    __tablename__ = 'ingrediente'

    IDINGREDIENTE = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(100))
    recetas = relationship("RecetaIngrediente",back_populates="ingrediente")



class Receta(Base):
    __tablename__ = 'receta'

    IDRECETA = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String(100))
    ingrediente_receta  = relationship("RecetaIngrediente", back_populates="receta")


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


