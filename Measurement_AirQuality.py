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

times = []
pm1 = []
pm25 = []
pm10 = []

port=serial.Serial('/dev/serial0')

start_time = time.time()
run_time = 1
stop_time = start_time + run_time
current_time = time.time()

with open('Air.csv', 'w') as f:
    header = ['Time', 'PM 1', 'PM 2.5','PM 10']
    writer = csv.writer(f)
    writer.writerow(header)
    while current_time < stop_time:
        current_time = time.time()
        
        port.read(32)
        data = port.read(32)
    
        pm1 = int.from_bytes(data[4:6],byteorder='big')
        pm25 = int.from_bytes(data[4:6],byteorder='big')
        pm10 = int.from_bytes(data[4:6],byteorder='big')
    
        current_time = time.time()
    
        print(pm1)
        print(pm25)
        print(pm10)
    
        #times.append(current_time)
        #temperatures.append(temp)
        #pressures.append(pressure)
        #humidities.append(humidity)
    
        writer.writerow([current_time,pm1,pm25,pm10])
    
        time.sleep(1)

#data = [times, temperatures, pressures, humidities]
    
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

