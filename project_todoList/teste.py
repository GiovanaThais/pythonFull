from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date 

app = FastAPI()

class Todo(BaseModel):
    task : Optional[str] 
    realized : bool
    time : Optional[date]

lista = []

@app.post('/create')
def create(todo: Todo):
    try:
        lista.append(todo)
        return {'status': 'sucesso'}
        
    except:
        return {'status': 'error'}

@app.get('/list')
def listAll(options: int = 0):
    if options == 0:
        return lista

    elif options == 1:
        return list(filter(lambda x: x.realized == False, lista))

    elif options == 2:
        return list(filter(lambda x: x.realized == True, lista))

@app.get('/listItem/{id}')
def listItems(id: int):
    try:
        return listItems[id]
    except:
        return {'status': 'error'}

@app.post('/newStatus')
def newStatus(id: int):
    try:
        lista[id].realized = not lista[id].realized
        return {'status': 'success'}
    except:
        return {'status': 'error'}

@app.post('/delete')
def delete(id: int):
    try:
        del lista[id]
        return {'status': 'success'}
    except:
        return {'status': 'error'}
