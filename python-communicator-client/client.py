import socket

addr = ('127.0.0.1', 12345) # toto je tuple
message = 'Hello my friend'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(message.encode('utf-8'), addr)
