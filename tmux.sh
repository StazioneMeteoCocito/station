#!/bin/bash
echo " [stationWrapper] Starting station main software" | xargs -d"\n" -I {} date +"%Y-%m-%d %H:%M:%S {}" >> /home/pi/station.log
tmux new -s StazioneMeteo -d /home/pi/Desktop/station/boot.sh
# Saved in crontab (root)
