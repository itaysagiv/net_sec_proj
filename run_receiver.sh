#!/bin/bash

IP="132.73.202.38" #ip for input from the encryptor
PORT="5555" #port for input from the encryptor
PROTO="udp"

clear

xterm -e vlc $PROTO://@$IP:$PORT 

#xterm -e python decryption_server.py $IP $PORT 127.0.0.1 8888
