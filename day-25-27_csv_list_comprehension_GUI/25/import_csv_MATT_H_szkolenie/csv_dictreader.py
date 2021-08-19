import csv
FILE = r'_temporary.csv'

FIELDNAMES = ['Sepal Length', 'Sepal Width',
              'Petal Length', 'Petal Width', 'Species']

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

with open(FILE, mode='w') as file:
    file.write(DATA)

result: list = []

# Solution
with open(FILE) as file:
    header = file.readline()
    reader = csv.DictReader(file, fieldnames=FIELDNAMES, quoting=csv.QUOTE_NONE)
    for line in reader:
        result.append(line)