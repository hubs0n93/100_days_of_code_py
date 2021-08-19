numbers = [1, 2, 3]

new_list = []
for i in numbers:
    new_list.append(i + 1)

print(new_list)
print("or one liner: 'new_numbers = [new_item for item in list]")

new_numbers = [item + 1 for item in numbers]
print(new_numbers)

name = "Hubert"

spell = [letter for letter in name]
print(spell)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
big_names = [name.upper() for name in names if len(name) > 4]
print(big_names)
print("\n")
# (x := 1) taka skladnia sprawia ze x przyjmnie wartosc 1 ale równocześnie jest zwracana
big_names_training = [big_name for name in names if (big_name := name.upper())]
print("\n  *******   output - szkoelnie python **********\n")
print('big_names_training = [big_name for name in names if (big_name := name.upper())]')
print(big_names_training)
print()
print("refactor zadania z dlugosci")
n = [imie for name in names if (imie:= name) and (len(name) > 4)]
print('n = [imie for name in names if (imie:= name) and (len(name) > 4)]')
print(n)