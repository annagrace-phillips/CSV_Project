#add dates to the x axis of the graph

import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#the enumerate() function returns both the index of each item and the value of each
#item as you loop through a list.

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
dates = []

mydate = "2018-07-01"
converted_date = datetime.strptime(mydate, "%Y-%m-%d")

# print(converted_date)

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

#print(highs)
#print(dates)
#plot highs on a chart

import matplotlib.pyplot as plt

fig = plt.figure()
fig.autofmt_xdate()

plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

plt.show()