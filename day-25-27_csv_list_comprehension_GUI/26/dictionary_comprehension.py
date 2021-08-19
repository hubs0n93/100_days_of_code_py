# FORMULA
# new_dict ={new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

# new_dict ={new_key - {name}:new_value - {random} for item - {name} in list - {names}}
students_score ={name:random.randint(0,100) for name in names}
print(students_score)

print("\nnext operation: new_dict = {new_key:new_value for (key,value) in dict.items()}")
passed_students = {key:value for (key,value) in students_score.items() if value > 60}
print(passed_students)
