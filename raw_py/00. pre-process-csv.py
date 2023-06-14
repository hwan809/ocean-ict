import csv
from datetime import datetime

FUKSHIMA_TIME = datetime(2012, 3, 12, 15, 36)

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

    # save
    csv_writer(
        [diff_seconds, distance, value, latitude, longitude],
        after_writer if diff_seconds >= 0 else before_writer
    )

file.close()
before_file.close()
after_file.close()