#!/bin/bash
while :
do
	python3 radioupdate.py
	espeak -s 120 -f bullEN
	espeak -v it -s 120 -f bullIT
	cat radio | minimodem --tx rtty
	sleep 10m
done
