from time import sleep
from machine import Pin, I2C
from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960

bus = I2C(-1, scl = Pin(22), sda = Pin(21))

try:
  apds = APDS9960(bus)
except:
  print("failed to initilize apds, check connection")


apds.enableLightSensor()
while True:
  sleep(1)
  amb =  apds.readAmbientLight()
  red = apds.readRedLight()
  green = apds.readGreenLight()
  blue = apds.readBlueLight()
  print("Ambience: ", amb, "  Red: ", red, "  Green: ", green, "  Blue: ", blue)
