import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

file_title = 'data/death_valley'
file_title = 'data/sitka_weather'
place_name = ''

reader = csv.reader
header_row = next(csv_file)

print(header_row)
date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

highs = []
lows = []
dates = []

mydate = "2018-07-01"
converted_date = datetime.strptime(mydate, "%Y-%m-%d")

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

import matplotlib.pyplot as plt

fig = plt.figure()
fig, ax = plt.subplots(2,2)

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
fig.autofmt_xdate()

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title(file_title, fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which= 'major', labelsize=12)

fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="dates")
a[0].fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)


for ax in a.flat:
    ax.label_outer()

a[1].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")
a[1].fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)


plt.show()