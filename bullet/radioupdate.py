import json
from datetime import datetime as dt
import datetime
def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
def IFormat(data, f):
    return format(data, f).replace("."," virgola ")
f = open("../storedData/last.json")
data = json.loads(f.read())
f.close()

n = dt.now()
with open("bullEN","w") as en:
    en.write(
        """
Cocito Weather Station

FM broadcasting service

This is the bulletin of """+custom_strftime('%A, the {S} of %B, %Y, %H hours and %M minutes', n)+"""

temperature: """+format(data["T"], ".2f")+""" degrees celsius;
humidity: """+format(data["H"], ".2f")+""" percent;
pressure: """+format(data["P"], ".2f")+""" hectopascals;
pm 10: """+format(data["PM10"], ".2f")+""" micrograms over cubic meter;
pm 2.5: """+format(data["PM25"], ".2f")+""" micrograms over cubic meter;
Smoke and flammable vapours: """+format(data["S"], ".2f")+""" micrograms over cubic meter;

Remain tuned for the next bulletin, in 10 minutes

Follows the italian version of this bulletin, then the encoded data for radio teletype terminals
        """
    )

daysIT = ["Lunedì","Martedì", "Mercoledì","Giovedì","Venerdì", "Sabato", "Domenica"]
monthsIT = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
with open("bullIT","w") as it:
    it.write(
        """
Stazione Meteorologica del Liceo Scientifico Statale Leonardo Cocito

Servizio di trasmissione FM

Bollettino di """+daysIT[n.weekday()]+", "+n.strftime("%d ")+monthsIT[int(n.strftime("%m"))-1]+" "+n.strftime("%Y")+""", ore """+n.strftime("%H e %M")+"""

temperatura: """+IFormat(data["T"], ".2f")+""" cielsius;
umidità: """+IFormat(data["H"], ".2f")+"""  percento;
pressione: """+IFormat(data["P"], ".2f")+"""  ettopascàl;
pm 10: """+IFormat(data["PM10"], ".2f")+"""  microgrammi su metro cubo;
pm 2 virgola 5: """+IFormat(data["PM25"], ".2f")+"""  microgrammi su metro cubo;
fumo e vapori infiammabili: """+IFormat(data["S"], ".2f")+"""  microgrammi su metro cubo;

Rimanete sintonizzati per il prossimo bollettino tra 10 minuti

Segue la trasmissione dei dati per le telescriventi radio

        """
    )
rp = open("../storedData/report.txt","r")
report = rp.read()
rp.close()
with open("radio","w") as radio:
    radio.write(
        """
CQ CQ CQ DE Stazione Meteo Cocito Alba
FREQUENCIES 108.1 kHz
RYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRY
CQ CQ CQ DE Stazione Meteo Cocito Alba
FREQUENCIES 108.1 kHz
RYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRY
CQ CQ CQ DE Stazione Meteo Cocito Alba
FREQUENCIES 108.1 kHz
RYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRYRY
ZCZC
STAZ METEO COCITO
RTTY WEATH BULLET
LAT 44° 41' 46.7124'' N
LON 8° 1' 48.7632'' E

"""+n.isoformat()+"""

TEMP """+format(data["T"], ".2f")+""" C
HUM """+format(data["H"], ".2f")+""" %
PRES """+format(data["P"], ".2f")+""" hPa
PM10 """+format(data["PM10"], ".2f")+""" ugm3
PM2.5 """+format(data["PM25"], ".2f")+""" ugm3
SMOKE """+format(data["S"], ".2f")+""" ugm3

"""+report+"""

NEXT 10 min 
NEXT """+(n + datetime.timedelta(minutes=10)).isoformat()+"""


NNN
NNN
NNN
"""
    )
