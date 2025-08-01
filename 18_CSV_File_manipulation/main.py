# with open("weather_data.csv") as file:
#     words = file.readlines()
#     print(words)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#

import pandas
data = pandas.read_csv("weather_data.csv")
