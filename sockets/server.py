from email.mime import message
import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(HOST, PORT)

sock.listen(5)

while True:
    newSocket,_ = sock.accept()
    message = newSocket.recv(1024)
    newSocket.send(b'ok')