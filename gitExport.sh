dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
cd $dir
bash infofile.sh | tee "storedData/report.txt"
python3 spacepos.py
cd bullet
bash *.sh
cd ..
cd storedData
lastDir=$(find 2* -type d | sort | tail -n 1)
t=$(cat $lastDir"/temperature.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
h=$(cat $lastDir"/humidity.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
p=$(cat $lastDir"/pressure.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
s=$(cat $lastDir"/smoke.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
pm10=$(cat $lastDir"/pm10.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
pm25=$(cat $lastDir"/pm25.csv" | tail -n 1 | awk -F","  '{ print $2 } ')
utciso=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
printf '{\n"T":'$t',\n"H":'$h',\n"P":'$p',\n"PM10":'$pm10',\n"PM25":'$pm25',\n"S":'$s',\n"utciso":"'$utciso'"\n}' | tee last.json
git pull
git add *
git commit -m "Regular data update"
git push origin main
