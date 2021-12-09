import gps
import csv
import time
import sys

sys.argv

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

if len(sys.argv) > 1:
		sleep_time = int(sys.argv[1])


time.sleep(sleep_time*60)
while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        #print(report)
        with open("GPS Data", 'w') as f:
            header = ['Time', 'Longitude', 'Latitude']
            writer = csv.writer(f)
            writer.writerow(header)
            if report['class'] == 'TPV':
                if hasattr(report, 'time'):
                    print(report.time)
            if report['class'] == 'TPV':
                if hasattr(report, 'lon'):
                    print(report.lon)
            if report['class'] == 'TPV':
                if hasattr(report, 'lat'):
                    print(report.lat)
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
    time.sleep(1)
