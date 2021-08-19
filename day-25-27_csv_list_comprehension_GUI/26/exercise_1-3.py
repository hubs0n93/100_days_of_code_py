numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [num ** 2 for num in numbers]
# Write your code 👆 above:

print(squared_numbers)
# *******************************************************************************************
#    ******** exercise 2
numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:
result = [num2 for num2 in numbers2 if num2 % 2 == 0]
# Write your code 👆 above:

print(result)
# *******************************************************************************************
with open("file1.txt") as file1:
    list_1 = file1.readlines()
with open("file2.txt") as file2:
    list_2 = file2.readlines()

result2 = [int(number) for number in list_1 if number in list_2]
# Write your code above 👆
print("Exercise 3 result:")
print(result2)
