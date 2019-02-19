list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 7, 6, 9]
exclude = list()
for number in list1:   
    if number in list2:
        exclude.append(number)
for number in exclude:
    list1.remove(number)
print(list1)