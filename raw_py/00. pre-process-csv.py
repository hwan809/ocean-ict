import csv
import math
from datetime import datetime

FUKSHIMA_TIME = datetime(2012, 3, 12, 15, 36)
FUKUSHIMA_LATITUDE = 37.422972
FUKUSHIMA_LONGITUDE = 141.032917

def csv_writer(data, writer):
    writer.writerow(data)

# open measurements csv file
file = open('fukushima-dataset/measurements_modified.csv','r')
reader = csv.DictReader(file)

# output two files, depending on time
before_file = open('fukushima-dataset/before_measurements_modified.csv', 'w', newline="")
after_file = open('fukushima-dataset/after_measurements_modified.csv', 'w', newline="")

before_writer = csv.writer(before_file)
after_writer = csv.writer(after_file)

for line in reader:
    # retrieves captured_time, radiation value (cpm), distance to fukushima

    captured_time = line['Captured Time']
    value = line['Value']
    distance = line['Distance To Fukushima in Km']

    # map position for visualization
    latitude = line['Latitude']
    longitude = line['Longitude']

    # calculate time from incident
    captured_datetime = datetime.strptime(
        captured_time, 
        "%Y-%m-%d %H:%M:%S"
    )
    diff_seconds = (captured_datetime - FUKSHIMA_TIME).total_seconds()

    # calculate vector for circular data (angle)
    dx = float(latitude) - FUKUSHIMA_LATITUDE 
    dy = float(longitude) - FUKUSHIMA_LONGITUDE

    vec_angle = math.atan2(dy, dx)

    vec_sin = math.sin(vec_angle)
    vec_cos = math.cos(vec_angle)

    # save-
    csv_writer(
        [diff_seconds, distance, value, latitude, longitude, vec_cos, vec_sin],
        after_writer if diff_seconds >= 0 else before_writer
    )

file.close()
before_file.close()
after_file.close()