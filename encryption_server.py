import socket
import sys
import time
from Crypto.Cipher import AES
from functools import partial

BUFF = 1500

# AES parameters
key = '0123456789abcdef'
mode = AES.MODE_CBC
IV = '0123456789abcdef'
encryptor = AES.new(key, mode,IV)

#recieve dest address from terminal
#ffmpeg_address = (sys.argv[1],int(sys.argv[2]))
#dest_address = (sys.argv[3],sys.argv[4])
server_address = ''
in_port = int(sys.argv[1])
out_port = int(sys.argv[2])

# Create a listening socket for input
sock_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print >>sys.stderr, 'input from %s port %s' % (server_address,in_port)
sock_in.bind((server_address,in_port))
sock_in.listen(1)

#create a sending socket for encrypted output
sock_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print >>sys.stderr, 'output to %s port %s' % (server_address,out_port)
sock_out.bind((server_address,out_port))
sock_out.listen(1)

#waiting for connection
print >>sys.stderr, 'waiting for a connection...'
connection, client_address = sock_out.accept()

while True:
	try:
		data = sock_in.recv(BUFF)
		if data:
			print >>sys.stderr, 'recieving stream packet'
			data = data + '/0'*(data.len()%16)	#padding with zeros for AES encryption
			enc_data = encryptor.encrypt(data)
			connection.sendall(enc_data)
		else:
			encryptor = AES.new(key, mode,IV)
	#stops at CTRC + C signal
	except KeyboardInterrupt:
		print >>sys.stderr, 'closing server'
		connection.close()
		sock_in.close()
		sock_out.close()
		break