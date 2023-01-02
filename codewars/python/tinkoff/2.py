number_age = input()
list_of_winners = []
for people in range(int(number_age)):
    list_of_winners.append(input())

dict_of_winners = {}
for i in list_of_winners:
    key = "_".join(sorted(set(i.split())))
    if key in dict_of_winners:
        dict_of_winners[key] += 1
    else:
        dict_of_winners[key] = 1


sort_dict = (sorted(dict_of_winners.items(), key=lambda item: item[1]))
print(sort_dict[-1][1])


"""
5
MIKHAIL VLADISLAV GRIGORY
VLADISLAV MIKHAIL GRIGORY
IVAN ILYA VLADIMIR
ANDREY VLADIMIR ILYA
VLADIMIR IVAN ANDREY
"""