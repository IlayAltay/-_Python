#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# SI7021
 
import smbus
import time


def get_temp():
    bus.write_byte(0x40, 0xF3)
    time.sleep(0.3)
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)
    cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    return round(cTemp,2)



# Get I2C bus (Номер шины в разных МК может отличаться. В PI3 - 1)
bus = smbus.SMBus(1)
 
# SI7021 address, 0x40(64)
# 0xF5(245)	Select Relative Humidity NO HOLD master mode
bus.write_byte(0x40, 0xF5)
 
time.sleep(0.3)
 
# SI7021 address, 0x40(64)
# Read data back, 2 bytes, Humidity MSB first
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)
 
# Convert the data
humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
 
time.sleep(0.3)
 
# SI7021 address, 0x40(64)
#		0xF3(243)	Select temperature NO HOLD master mode
bus.write_byte(0x40, 0xF3)
 
time.sleep(0.3)
 
# SI7021 address, 0x40(64)
# Read data back, 2 bytes, Temperature MSB first
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)
 
# Convert the data
cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
fTemp = cTemp * 1.8 + 32
 
# Output data to screen
#print ("Влажность: %.2f %%" %humidity)
#print ("Температура C: %.2f" %cTemp)
#print "Температура F: %.2f" %fTemp