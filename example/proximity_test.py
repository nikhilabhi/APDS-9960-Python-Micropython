from time import sleep
from machine import Pin, I2C
from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960

bus = I2C(-1, scl = Pin(22), sda = Pin(21))

try:
  apds = APDS9960(bus)
except:
  print("failed to initilize apds, check connection")
  

print("Proximity Sensor Test")
print("=====================")
apds.enableProximitySensor()

oldvalue = -1
while True:
    sleep(0.25)
    value = apds.readProximity()
    if value != oldvalue:
        print("proximity={}".format(value))
        oldvalue = value
