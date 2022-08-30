import requests


retorna = requests.post('https://128.0.0.1:8000/user', params={'id':4, 'name': 'Test', 'password': 'minhasenha1'})

print(retorna.json())