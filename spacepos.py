from sense_hat import SenseHat
import json
import datetime
sense = SenseHat()
position = {}
acceleration = sense.get_accelerometer_raw()
o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
x = acceleration['x']
y = acceleration['y']
z = acceleration['z']
position = {"time":datetime.datetime.now().astimezone().isoformat(),"accelleration":{"x":x, "y":y, "z":z}, "position":{"pitch":pitch,"roll":roll,"yaw":yaw}}
f = open("storedData/position.json","w+")
f.write(json.dumps(position,indent = 4))
f.close()
