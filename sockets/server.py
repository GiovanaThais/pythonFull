from email.mime import message
import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(5)

while True:
    newSock, _ = sock.accept()
    message = newSock.recv(1024).decode() #recebe mensagem em binario
    newSock.send(b'ok')