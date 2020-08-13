#!/usr/bin/python
from max6675 import MAX6675, MAX6675Error
import time


cs_pin = 5
clock_pin = 6
data_pin = 16
units = "c"
thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
running = True
while(running):
    try:            
        try:
            tc = thermocouple.get()
            print("tc: {}".format(tc))
            f = open("/home/pi/fireplace-max6675/max6675.log", "w")
            f.write(str(tc))
            f.close
        except MAX6675Error as e:
            tc = "Error: "+ e.value
            #running = False
            print("Etc: {}".format(tc))
            g = open("/home/pi/fireplace-max6675/max6675.log", "w")
            g.write(str(tc))
            g.close
        time.sleep(5)
    except KeyboardInterrupt:
        running = False
thermocouple.cleanup()
