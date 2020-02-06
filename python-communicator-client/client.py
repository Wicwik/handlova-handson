import socket

CLIENT_IP = '127.0.0.1'
CLIENT_PORT = 12345
MESSAGE = 'Hello my friend'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE.encode('utf-8'), (CLIENT_IP, CLIENT_PORT))
