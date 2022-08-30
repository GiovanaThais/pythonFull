from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    id: int
    name: Optional[str]
    password: str


listUsers = [
    User(id=1, name = 'Giovana', password ='senha123'),
    User(id=2, name = 'Thais', password ='senha12'),
    User(id=3, name = 'Eduardo', password ='minhasenha')
]

#endpoit para cadastrar
@app.post('/user') 
def main(user: User):
    listUsers.append(user)
    return user

@app.get('/userList')
def main():
    return listUsers

@app.get('/')
def root():
    return {'message': 'Home'}

@app.get('/cadastro')
def cadastro():
    return {'message': 'cadastro'}

@app.get('/login')
def login():
    return {'message': 'login'}


# users = [(1, 'joao', 'minhasenha1'), (2, 'maria', 'minhasenha2')]
# @app.get('/user/{id}')
# def main(id: int):
#     for i in users:
#         if i[0] == id:
#             return i
#     return "usuario nao cadastrado"

# @app.post('/user/')
# def main(name):
#     for i in users:
#         if i[0] == name:
#             return i
#     return "usuario nao cadastrado"