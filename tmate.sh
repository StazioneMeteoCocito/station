!/bin/bash
echo " [tmate] Starting tmate remote access daemon" | xargs -d"\n" -I {} date +"%Y-%m-%d %H:%M:%S {}" >> /home/pi/station.log
tmate -F &
