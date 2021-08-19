import pandas


csv_file = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(csv_file)

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def main():
    to_spell = input("Enter a word: ").upper()
    try:
        spelt = [data_dict[letter] for letter in to_spell]
    except KeyError:
        print("Sorry, only letters from alphabet can be spelling out")
        main()
    else:
        print(spelt)


main()
