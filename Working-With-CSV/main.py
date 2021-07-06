# how to use csv library
# import csv
# with open("weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         try:
#             temp = int(row[1])
#             temperatures.append(temp)
#         except ValueError:
#             continue
# print(temperatures)
import pandas

# how to read data in pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data.temp)
# print(data)

# how to convert data to dict using pandas
# data_dict = data.to_dict()
# print(data_dict)

# how to convert a series to list
# data_list = data["temp"].to_list()
# print(data_list)

# finding average of temperatures
# print(data["temp"].mean())

# finding max value of temperatures
# print(data["temp"].max())

# working with rows
# print(data[data.day == "Monday"])

# printing the row where the temperature is max
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# Working inside the row
# monday = data[data.day == "Monday"]
# print(monday.condition)

# fetching the temperature on monday and converting it to fahrenheit
# mon_temp = int(monday.temp)
# print((mon_temp * (9/5))+32, "F")

# how to create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# assignment - create a new csv file containing number of squirrel in each color category
# Method - 1
squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
colors = squirrel["Primary Fur Color"].to_list()
gray = black = red = 0
for color in colors:
    if color == "Gray":
        gray += 1
    elif color == "Black":
        black += 1
    elif color == "Cinnamon":
        red += 1
color_dict = {
    "Colors": ["Gray", "Red", "Black"],
    "Counts": [gray, red, black]
}
data = pandas.DataFrame(color_dict)
data.to_csv("squirrel_colors_count.csv")

# Method - 2
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
squirrel_color_dict = {
    "Colors": ["Gray", "Red", "Black"],
    "Counts": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
data = pandas.DataFrame(squirrel_color_dict)
data.to_csv("squirrel_counts.csv")
