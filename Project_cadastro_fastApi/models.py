from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "aulapythonfullfastapi"
PORT = "3308"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    nome = Column(String(50))
    id = Column(Integer, primary_key=True)
    user = Column(String(20))
    senha = Column(String(10))

class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

Base.metadata.create_all(engine)
