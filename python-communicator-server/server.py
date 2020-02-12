import socket

ACK = 1
MSG = 1 << 1

def accept_packets():
    packets_accepted = 0;
    full_message = ''

    while True:
        data, addr = sock.recvfrom(1518) # velkost buffera
        packets_accepted = packets_accepted + 1
        print('Recieved ' + str(packets_accepted) + '. packet:', end='')
        print(' - From: ' + addr[0] + ':' + str(addr[1]))

        type = data[0:2]
        data_size = data[2:4]
        message = data[4:]

        if int.from_bytes(type, byteorder='big') == ACK:
            break;

        full_message += message.decode('utf-8')

    print('The message is: ' + full_message)

    info = (addr, packets_accepted)
    return info

def send_ack_to_client(packets_accepted, client_addr):
    type_byte = ACK.to_bytes(2, byteorder='big')
    size_byte = (2).to_bytes(2, byteorder='big')
    data_byte = packets_accepted.to_bytes(2, byteorder='big')

    packet = type_byte + size_byte + data_byte

    sock.sendto(packet, client_addr)


input_port = int(input('Listening port: '), 10)

addr = ('0.0.0.0', input_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(addr)

print('Starting server...')
info = accept_packets()
client_addr = info[0]
packets_accepted = info[1]

send_ack_to_client(packets_accepted, client_addr)

sock.close()
