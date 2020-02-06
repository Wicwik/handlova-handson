import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print('Recieved message: ' + data.decode('utf8'))
    print('From: ' + addr[0] + ':' + str(addr[1]))
