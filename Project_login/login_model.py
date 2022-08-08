from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


CONN = "sqlite:///projeto2.db"
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base


class Category:
    __tablename__ = 'Categoria'
    id = Column(Integer, primary_key=True)
    category = Column(String(30))

class Pessoa(Base):
        __tablename__ = 'Pessoa'
        id = Column(Integer, primary_key = True)
        name = Column(String(50))
        user = Column(String(20))
        email = Column(String(100))
        password = Column(String(100))
        idCategory = Column(Integer, ForeignKey(Category.id))

Base.metadata.create.all(engine)