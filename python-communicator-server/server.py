import socket

ACK = 1
MSG = 1 << 1
FILE = 1 << 2

addr = ('127.0.0.1', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(addr)

# while True:
#     data, addr = sock.recvfrom(1024) # velkost buffera
#     print('Recieved message: ' + data.decode('utf8'))
#     print('From: ' + addr[0] + ':' + str(addr[1]))


sock.close()
