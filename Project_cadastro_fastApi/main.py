from fastapi import FastAPI
from models import CONN, Pessoa, Tokens
from secret import token_hex

app = FastAPI()

def conectaBancos():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.route('/cadastro/')
def cadastro(nome: str, user: str, senha: str):
    session = conectaBancos()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()
    if len(usuario) == 0: 
        x = Pessoa(nome = nome, usuario = usuario, senha = senha)
        session.add(x)
        session.commit()
        return {'status': 'success'}
    elif len(usuario) > 1:
        return {'status': 'usuario ja cadastrado'}

@app.post('/login')
def login(usuario: str, senha: str):
    session = conectaBancos()
    user = session.query(Pessoa).filter_by(username=usuario, senha=senha)
    if len(user) == 0:
        return {'status': 'usuario inexistente'}

    while True:
        token = token_hex(50)
        tokenExists = session.query(Tokens).filter_by(token=token).all()
        if len(tokenExists) == 0:
            pessoaExiste = session.query(Tokens).filter_by(id_pessoa= user[0].id).all()
            if len(pessoaExiste) == 0:
                novoToken = Tokens(id_pessoa= user[0].id, token =token)
                session.add(novoToken)
            elif len(pessoaExiste) > 0:
                pessoaExiste[0].token = token

            session.commit()
        break
    return token
            
