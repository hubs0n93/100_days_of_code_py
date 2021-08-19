# data = []

# with open("weather_data.csv") as file:
#     data = file.readlines()


# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file,)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1].strip("'")))
#
# print(temperatures)

#PANDAS

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print()
avr = round(sum(temp_list)/len(temp_list))
print(avr)
print("it is the same that: series.mean()")
print(round(data["temp"].mean()))
print(data["temp"].max())

print("Open series in two method, dict: data['temp'], or object: data.temp")
print(data.temp)

print("searching in data")
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp_on_monday = int(monday.temp)
temp_on_fahrenheit = (temp_on_monday * 1.8) + 32
print(temp_on_monday)
print(temp_on_fahrenheit)

#Create a dataFrame from scratch
data_dictionary = {
    "students": ["Amy", "James", "Bubi"],
    "scores": [76, 56, 102]
}

my_data = pandas.DataFrame(data_dictionary)
print(my_data)
my_data.to_csv("my_file.csv", index=False)