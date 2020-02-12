import socket

ACK = 1
MSG = 1 << 1

def accept_packets():
    packets_accepted = 0;
    while True:
        data, addr = sock.recvfrom(1518) # velkost buffera
        packets_accepted = packets_accepted + 1
        print('Recieved ' + str(packets_accepted) + '. packet:', end='')
        print(' - From: ' + addr[0] + ':' + str(addr[1]))
        print(data[0:2])

addr = ('127.0.0.1', 12345)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(addr)

accept_packets()

sock.close()
