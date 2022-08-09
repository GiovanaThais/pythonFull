import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send(b"enviado") #converte a "str" em binario 

confirmed = sock.recv(1024) #o client recebe inform do servidor e retorna ok
if confirmed == b'ok':
    print('mensagem recebida')
