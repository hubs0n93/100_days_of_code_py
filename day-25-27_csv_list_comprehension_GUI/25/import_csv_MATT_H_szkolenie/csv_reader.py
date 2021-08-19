import csv

FILE = r'_temporary.csv'

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

with open(FILE, mode='w') as file:
    file.write(DATA)

# list[tuple]: data from file (note the list[tuple] format!)
result = []

# Solution
with open(FILE) as file:
    reader = csv.reader(file)
    for row in reader:
        result.append(tuple(row))