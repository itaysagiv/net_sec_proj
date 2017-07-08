import socket
import sys
import time
from Crypto.Cipher import AES
from functools import partial

key = '0123456789abcdef'
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, '0123456789abcdef')

BUFF = 256

file_name = sys.argv[1]

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

c = 0
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        with open(file_name, 'rb') as openfileobject:
            for chunk in iter(partial(openfileobject.read, BUFF), ''):
                print >>sys.stderr, 'sending packet #%d' % c + '\t\tsize of %d byte' % len(chunk)
                c=c+1
                if len(chunk)<BUFF:
                    chunk = chunk + '\0'*(BUFF - len(chunk))
                try:
                    connection.sendall(encryptor.encrypt(chunk))
                except:
                    print >>sys.stderr, 'connection ended unexpectedly'
                    break
                time.sleep(0.001)
        # Receive the data in small chunks and retransmit it

            
    finally:
        # Clean up the connection
        connection.close()
        c=0