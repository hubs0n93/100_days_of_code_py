student_dict ={
    "student": ['Angela', 'Bubert', 'Lily'],
    "score": [56, 76, 98],
}

# Looping thorugh dict:
for (key, value) in student_dict.items():
    print(value)

# *********************************************************************************************
import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

# *********************************************************************************************
print("\nitter DF like a dict, key returns name of column, value returns all values")
print("key - column name")
for (key, value) in student_df.items():
    print(key)
    
print("*************************")
print("value - values column by column")
for (key, value) in student_df.items():
    print(value)

# ********************************************************************
print("\n Data Frame iterrows")
for (index, row) in student_df.iterrows():
    print(row)

# ********************************************************************
print("\n Take a concrete value:")
for (index, row) in student_df.iterrows():
    if row.student == "Bubert":
        print(row.score)