#!/bin/bash
# to be run as root
echo " [nightCleanup] Trimming log to last 500 rows" | xargs -d"\n" -I {} date +"%Y-%m-%d %H:%M:%S {}" >> /home/pi/station.log
echo "$(tail -n 500 /home/pi/station.log)" > /home/pi/station.log
killall python3
echo " [nightCleanup] Killing python and waiting a bit" | xargs -d"\n" -I {} date +"%Y-%m-%d %H:%M:%S {}" >> /home/pi/station.log
sleep 100
echo " [stationWrapper] Daily power cycle" | xargs -d"\n" -I {} date +"%Y-%m-%d %H:%M:%S {}" >> /home/pi/station.log
reboot
