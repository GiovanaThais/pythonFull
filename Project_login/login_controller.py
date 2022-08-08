from sqlalchemy import create_engine
import hashlib

from Project_login.login_model import Pessoa #proteção de dados de senha


def retorna_session():
    CONN = 'sqlite:///projeto2.db'
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def verificar_dados(cls, name, email, password):
        if len(name) > 60 or len(name) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(password) > 100 or len(password) < 6:
            return 4
        return 1

    @classmethod
    def cadastrar(cls, name, email, password):
        session = retorna_session()
        user = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(user) > 0:
            return 5

        dados_verificaciones = cls.verificar_dados(name, email, password)

        if dados_verificaciones != 1:
            return dados_verificaciones

        try:
            password = hashlib.sha256(password.encode()).hexdigest()
            p1 = Pessoa(name=name, email=email, password=password)
            session.add(p1)
            session.commit()
            return 1

        except:
            return 3
