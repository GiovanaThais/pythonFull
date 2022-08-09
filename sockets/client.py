import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_)

sock.connect((HOST, PORT))

sock.send(b"enviado")

confirmed = sock.recv(1024)
if confirmed == b'ok':
    print('mensagem recebida')
