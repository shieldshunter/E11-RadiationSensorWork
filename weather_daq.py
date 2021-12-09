#Measures Temperature, Humidity, Pressure
# BME280 - Adafruit
# Write the data to a file - a time column, temperature, humidity, pressure
# - look up Adafruit CircuitPython BME280 module
# - update code to use that module

import time
import math
import numpy as np
import pandas as pd
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)

times = []
temperatures = []
pressures = []
humidities = []


start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()
while current_time < stop_time:
	current_time = time.time()
	temp = sensor.read_temperature()
	pressure = sensor.read_pressure()
	humidity = sensor.read_humidity()
	current_time = time.time()
	print(temp)
	print(pressure)
	print(humidity)
	times.append(current_time)
	temperatures.append(temp)
	pressures.append(pressure)
	humidities.append(humidity)
	time.sleep(1)
	
def average(num):

	avg = sum(num) / len(num)
	
	return avg



avg_temp = average(temperatures)
avg_pressure = average(pressures)
avg_humidity = average(humidities)

print("Temperature", avg_temp)
print("Pressure", avg_pressure)
print("Humidity", avg_humidity)

print(times)
print(temperatures)
print(pressures)
print(humidities)

#np_data = np.array(object: array_like, order={temperatures,pressures,humidities})
#savetxt('data.csv', data, delimiter=',')

list1 = [[times, temperatures, pressures, humidities]]
dataset = pd.DataFrame(list1, columns=['times','temperatures','pressures','humidities'])
print(dataset)
dataset.to_csv('AtmosReadings.csv')
	
