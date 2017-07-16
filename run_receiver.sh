#!/bin/bash

IP="127.0.0.1" #ip for input from the encryptor
PORT="5555" #port for input from the encryptor
PROTO="udp"

clear

xterm -e cvlc $PROTO://@127.0.0.1:8888 &

xterm -e python decryption_server.py $IP $PORT 127.0.0.1 8888
