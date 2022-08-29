import socket
import threading

HOST = '127.0.0.1'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala, message):
    for i in salas[sala]:
        if isinstance(message, str):
            message = message.encode()

        i.send(message)

def sendMessage(name, sala, client):
    while True:
        message = client.recv(1024)
        message = f"{name}: {message.decode()}" #decodificar mensagem
        broadcast(sala, message) #enviar mensagem para todos da sala

while True: #conecta os clientes
    client, addr = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    name = client.recv(1024).decode()
    if salas not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'{name} se conectou na sala {sala}! INFO {addr}')
    broadcast(sala, f'{name}: Entrou na sala!')
    #broadcast- enviar para todos da sala
    thread = threading.Thread(target=sendMessage,
                            args=(name, sala, client))
