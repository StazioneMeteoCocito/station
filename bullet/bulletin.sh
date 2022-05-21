#!/bin/bash
while :
do
	python3 radioupdate.py
	espeak -s 120 -f bullEN -w en.wav
	espeak -v it -s 120 -f bullIT -w it.wav
	cat radio | minimodem --tx rtty -f radio.wav
	ffmpeg -y -i en.wav -i it.wav -i radio.wav \
	-filter_complex '[0:0][1:0][2:0]concat=n=3:v=0:a=1[out]' \
	-map '[out]' bulletin.mp3
	rm *.wav
	mv bulletin.mp3 ../storedData/
	espeak -s 120 -f bullEN
	espeak -v it -s 120 -f bullIT
	cat radio | minimodem --tx rtty
	sleep 10m
done
