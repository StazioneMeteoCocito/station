# 2021, Mattia Mascarello, The MIT License
import serial
from Station import Station
import time
import random
from sense_hat import SenseHat
import datetime
import signal
sense = SenseHat()
s = Station()
running = False

def log(text):
    f = open("/home/pi/station.log", "a+")
    f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"  [pythonStation] "+text+"\n")
    f.close()
    

def stop(a,b):
    global running
    log("Gracefully handling death")
    running = False

signal.signal(signal.SIGINT, stop)
signal.signal(signal.SIGTERM, stop)

ttyflag = False
for i in range(10):
    try:
        log("Trying /dev/ttyACM"+str(i))
        ser = serial.Serial('/dev/ttyACM'+str(i), 9600, timeout=10)
        ttyflag = True
        break
    except:
        time.sleep(10)
if(not ttyflag):
    log("Arduino is dead, continuing with it disabled")

def get_sensors_serial(ser):
    print("Requesting data from arduino")
    ser.write(bytes(1))
    dataA = []
    for i in range(3):
        try:
            dataA.append(float(str(ser.readline()).split(",")
                         [1].replace("\\r\\n'", "")))
        except:
            print("Serial connection with arduino timed out")
            return False
    if(len(dataA) == 0):
        print("Arduino sent no data")
        return False
    return {"pm10": dataA[0], "pm2.5": dataA[1], "smoke": dataA[2]}

timeMeasure = 5*60

while running:
    try:
        print("New measurement")
        dts = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        allData = {"humidity": sense.get_humidity(), "temperature": sense.get_temperature_from_humidity(),
                   "pressure": sense.get_pressure(), "when": dts, "serialOk": False}
        s.record_humidity(allData["humidity"])
        print("Humidity {h:.2f}".format(h=allData["humidity"]))
        s.record_pressure(allData["pressure"])
        print("Pressure {p:.2f} hPa".format(p=allData["pressure"]))
        s.record_temperature(allData["temperature"])
        if ttyflag:
            arduino = get_sensors_serial(ser)
            if arduino:
                allData["serialOk"] = True
                s.record_pm10(arduino["pm10"])
                s.record_pm25(arduino["pm2.5"])
                s.record_smoke(arduino["smoke"])
                allData["pm10"] = arduino["pm10"]
                allData["pm2.5"] = arduino["pm2.5"]
                allData["smoke"] = arduino["smoke"]
                print("Arduino data - PM10: {pmt:.2f}, PM 2.5: {pmtw:.2f}, Smoke: {s:.2f}".format(
                    pmt=arduino["pm10"], pmtw=arduino["pm2.5"], s=arduino["smoke"]))
        log("Measurement taken")
        i = 0
        while i<timeMeasure and running:
            time.sleep(1)
            i += 1
    except Exception as e:
        print("EXCEPTION:")
        log("Error : "+str(e))
        print(e)
        i = 0
        while i<timeMeasure and running:
            time.sleep(1)
            i += 1
