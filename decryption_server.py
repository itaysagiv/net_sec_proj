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
decryptor = AES.new(key, mode,IV)

#recieve dest address from terminal
#ffmpeg_address = (sys.argv[1],int(sys.argv[2]))
#dest_address = (sys.argv[3],sys.argv[4])
server_address = (sys.argv[1],int(sys.argv[2]))
vlc_address = (sys.argv[3],int(sys.argv[4]))

# Create a listening socket for input
sock_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print >>sys.stderr, 'connecting...'
sock_in.connect(server_address)
print >>sys.stderr, 'input from %s port %s' % server_address

#create a sending socket for encrypted output
sock_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print >>sys.stderr, 'output to %s port %s' % (vlc_address)
sock_out.bind(vlc_address)
sock_out.listen(1)

while True:
	try:
		data = sock_in.recv(BUFF)
		if data:
			dec_data = decryptor.decrypt(data)
			sock_out.sendall(dec_data)
		else:
			decryptor = AES.new(key, mode,IV)
	#stops at CTRC + C signal
	except KeyboardInterrupt:
		connection.close()
		sock_in.close()
		sock_out.close()
		break