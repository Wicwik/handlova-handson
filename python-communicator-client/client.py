import socket
from io import StringIO

ACK = 1
MSG = 1 << 1
FILE = 1 << 2
HEADER_SIZE = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def prepare_data(data,  type, size):
    type_byte = type.to_bytes(2, byteorder='big')
    size_byte = size.to_bytes(2, byteorder='big')
    print(size_byte)
    data_byte = data.encode('utf-8')
    packet = type_byte + size_byte + data_byte

    return packet


def send_packet(data, size, dest, port):
    addr = (dest, port) # toto je tuple
    message = prepare_data(data, MSG, size)

    sock.sendto(message, addr)

input_ip = input('Zadaj cielovu IP: ')
input_port = int(input('Zadaj port: '), 10)
input_message = input('Zadaj spravu: ')
input_size = int(input('Zadaj max velkost dat v PDU: '), 10)

if len(input_message) > input_size:
    string_file = StringIO(input_message)
    while True:
        chunk = string_file.read(input_size)
        if len(chunk) > 0:
            send_packet(chunk, input_size, input_ip, input_port)
        if len(chunk) < input_size:
            break;
else:
    send_packet(input_message, input_size, input_ip, input_port)
