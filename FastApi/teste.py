import re
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

users = [(1, 'joao', 'minhasenha1'), (2, 'maria', 'minhasenha2')]
@app.get('/user/{id}')
def main(id: int):
    for i in users:
        if i[0] == id:
            return i
    return "usuario nao cadastrado"

@app.post('/user/')
def main(name):
    for i in users:
        if i[0] == name:
            return i
    return "usuario nao cadastrado"


@app.get('/')
def root():
    return {'message': 'Home'}

@app.get('/cadastro')
def cadastro():
    return {'message': 'cadastro'}

@app.get('/login')
def login():
    return {'message': 'login'}