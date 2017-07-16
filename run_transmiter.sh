#!/bin/bash

IP="192.168.10.103" #ip for out to decryption
PORT="5555" #port for out to decryption

PROTO="udp"
VIDEO_FILE="a.mp4"
VIDEO_TIME="2:00"

clear

xterm -hold -e python encryption_server.py 127.0.0.1 1234 $IP $PORT &

xterm -e ffmpeg -re  -i $VIDEO_FILE -c copy -ss 00:00:00  -t $VIDEO_TIME  -bsf:v h264_mp4toannexb -f mpegts $PROTO://127.0.0.1:1234
