#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Measures Temperature, Humidity, Pressure
# BME280 - Adafruit
# Write the data to a file - a time column, temperature, humidity, pressure
# - look up Adafruit CircuitPython BME280 module
# - update code to use that module

import csv
import time
import math
import board
import serial
import sys
from adafruit_bme280 import basic as adafruit_bme280

#sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

#Stuff from before
times = []
temperatures = []
pressures = []
humidities = []

#Air
pm1 = []
pm25 = []
pm10 = []

port=serial.Serial('/dev/serial0')

sys.argv

if len(sys.argv) > 1:
        run_time = int(sys.argv[1])
        if len(sys.argv) > 2:
                sleep_time = int(sys.argv[2])
                if len(sys.argv) > 3:
                        delay_time = int(sys.argv[3])
                        if len(sys.argv) > 4:
                                file_name = str(sys.argv[4])
#run_time = float(input('Runtime: '))

#sleep_time = int(input('Time Between Intervals:  '))

#delay_time = int(input('Delay Time: '))

total_run_time = delay_time + run_time

start_time = time.time()
stop_time = start_time + total_run_time
current_time = time.time()

with open(file_name, 'w') as f:
    header = ['Time', 'Temperature', 'Pressure','Humidity', 'PM 1', 'PM 2.5','PM 10']
    writer = csv.writer(f)
    writer.writerow(header)
    time.sleep(delay_time)
    while current_time < stop_time:
        current_time = time.time()
        
        port.read(32)
        data = port.read(32)
        
        temp = bme280.temperature
        pressure = bme280.pressure
        humidity = bme280.humidity
    
        pm1 = int.from_bytes(data[4:6],byteorder='big')
        pm25 = int.from_bytes(data[6:8],byteorder='big')
        pm10 = int.from_bytes(data[8:10],byteorder='big')
    
        current_time = time.time()
        
        print(temp)
        print(pressure)
        print(humidity)
    
        print(pm1)
        print(pm25)
        print(pm10)
    

    
        writer.writerow([current_time,temp,pressure,humidity,pm1,pm25,pm10])
    
        time.sleep(sleep_time)



