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
from adafruit_bme280 import basic as adafruit_bme280

#sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

times = []
temperatures = []
pressures = []
humidities = []


start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()

with open('test.csv', 'w') as f:
    header = ['Time', 'Temperature', 'Pressure','Humidity']
    writer = csv.writer(f)
    writer.writerow(header)
    while current_time < stop_time:
        current_time = time.time()
    
        temp = bme280.temperature
        pressure = bme280.pressure
        humidity = bme280.humidity
    
        current_time = time.time()
    
        print(temp)
        print(pressure)
        print(humidity)
    
        times.append(current_time)
        temperatures.append(temp)
        pressures.append(pressure)
        humidities.append(humidity)
    
        writer.writerow([current_time,temp,pressure,humidity])
    
        time.sleep(1)

data = [times, temperatures, pressures, humidities]
    
#with open('test.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    for value in data:
#        word = value
#        for num in word:
#            writer.writerow([num])

#import pandas as pd

#df = pd.DataFrame({'time': times, 'temperatures': temperatures, 'pressures': pressures, 'humidities': humidities})
#print(df)
#df.to_csv('test.csv', index=False, header=True)

#times_ls = []
#times_ls = list(times)

#rows = len(times)
#print(rows)
#i = 0


    #Establishes a CSV file
#with open('test.csv', 'w') as f:
 #   header = ['Time', 'Temperature', 'Pressure','Humidity']
 #   writer = csv.DictWriter(f, fieldnames = header)
 #   writer.writeheader()
    #Allows us to write the data into rows
  #  while i < rows:
  #      writer.writerow({'Time':times_ls[i],'Temperature':temperatures[i],'Pressure':pressures[i],'Humidity':humidities[i]})
  #          

