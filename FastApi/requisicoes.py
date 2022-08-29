import requests


retorna = requests.get('https://128.0.0.1:8000/user', "name": "joao")

print(retorna.json()['message'])