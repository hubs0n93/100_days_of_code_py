import pandas

central_park_csv = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(central_park_csv)

gray = central_park_csv[central_park_csv["Primary Fur Color" ] == "Gray"]
red = central_park_csv[central_park_csv["Primary Fur Color" ] == "Cinnamon"]
black = central_park_csv[central_park_csv["Primary Fur Color" ] == "Black"]

squirrels_counter = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(gray["Primary Fur Color"]), len(red["Primary Fur Color"]), len(black["Primary Fur Color"])]
}

sc_df = pandas.DataFrame(squirrels_counter)
sc_df.to_csv("squirrel_count")