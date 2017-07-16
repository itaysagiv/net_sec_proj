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
server_address = sys.argv[1]
in_port = int(sys.argv[2])
client_address = sys.argv[3]
out_port = int(sys.argv[4])

# Create a listening socket for input
sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print >>sys.stderr, 'input port %s' % in_port
sock_in.bind((server_address,in_port))

#create a sending socket for encrypted output
sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print >>sys.stderr, 'output port %s' % out_port

while True:
	try:
		data,addr = sock_in.recvfrom(BUFF)
		if data:
			if len(data) % 16:
				data = data + '\0'*(16 - (len(data) % 16))	#padding with zeros for AES encryption
			enc_data = encryptor.encrypt(data)
			sock_out.sendto(enc_data,(client_address,out_port))
	#stops at CTRC + C signal
	except KeyboardInterrupt:
		print >>sys.stderr, 'closing server'
		sock_in.close()
		sock_out.close()
		break
