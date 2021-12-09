import time
import csv
import RPi.GPIO as GPIO
from time import sleep
import math
import numpy as np
import sys
#7, 17, 11, 12
#^This is what the pins could possibly be
#This sets the GPIO pin to 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

sys.argv

if len(sys.argv) > 1:
		intervals = int(sys.argv[1])
		if len(sys.argv) > 2:
				delay_time = int(sys.argv[2])
				if len(sys.argv) > 3:
						file_name = str(sys.argv[3])



detection = 0
counts = []

#Function to detect when events occur
def superswaggy_function(channel):
	if GPIO.input(17): # if port detects a rise
		print("Rising Edge detected")
		global detection
		detection += 1
		
GPIO.add_event_detect(17, GPIO.RISING, callback=superswaggy_function)
	
with open(file_name, 'w') as f:
	header = ['Time', 'CPM']
	writer = csv.writer(f)
	writer.writerow(header)
	sleep(delay_time*60)
	for i in range(intervals):
		detection = 0
		sleep(60)
		current_time = time.time()
		counts.append(detection)
		writer.writerow([current_time, detection])
		

#start_time = time.time()
#stop_time = start_time + run_time
#current_time = time.time()

#while current_time < stop_time:
#	current_time = time.time()
#	
#	counts.append(detection)
#	sleep(1)
	
	
	
#sleep(run_time)

total_counts = sum(counts)
print(total_counts, "Total counts")
average_cpm = (sum(counts)/intervals)
print(average_cpm, "Average CPM")

#rint("count list", counts)
#rint("There were", detection,"counts over a period of", run_time, "seconds")
#rint("The Average CPS was", average_cps)





