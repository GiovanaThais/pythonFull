from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoa


def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
session = RetornaSession()
x = session.query(Pessoa).all() 
# fazendo SELECT
X = session.query(Pessoa).filter(Pessoa.nome == 'giovana')
x = session.query(Pessoa).filter_by(usuario = 'giovana', nome = 'giovana')
x = session.query(Pessoa).filter(or_(Pessoa.nome == 'giovana', Pessoa.usuario == 'giovana')).all() #SELECT pelo nome ou usuario

#fazendo UPDATE
x = session.query(Pessoa).filter(Pessoa.id == 12).all()
X[0].nome = 'thais'

# fazendo DELETE
x = session.query(Pessoa).filter(Pessoa.id == 12).delete()

print(x[0].nome)