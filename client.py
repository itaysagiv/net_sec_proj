import socket
import sys
from Crypto.Cipher import AES

BUFF = 256
server_address = sys.argv[1]
output = sys.argv[2]
key = '0123456789abcdef'
mode = AES.MODE_CBC
decryptor = AES.new(key, mode, '0123456789abcdef')

out_file = open(output,"wb")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (server_address, 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:
    while True:
        data = sock.recv(BUFF)
        if data:
            print >>sys.stderr, data
            out_file.write(data)
        else:
            print >>sys.stderr, 'no more data'
            break


finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
    out_file.close()