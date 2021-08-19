import csv
FILE = r'_temporary.csv'

DATA = [{'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'firstname': 'Rick', 'lastname': 'Martinez'},
        {'firstname': 'Mark', 'lastname': 'Watney'},
        {'firstname': 'Ivan', 'lastname': 'Ivanovic'},
        {'firstname': 'Melissa', 'lastname': 'Lewis'}]

# Solution
with open(FILE, 'w') as file:
        data = csv.DictWriter(file, fieldnames=['firstname', 'lastname'],
                          delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,
                          lineterminator='\n')

        data.writeheader()
        data.writerows(DATA)