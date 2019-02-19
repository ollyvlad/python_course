list = [2, 5, 4, 1, 8, 12, 18, 3]
for a in range(len(list)):
    if list[a] % 2 == 0:
        list[a] = list[a]/4
    else:
        list[a] = 2*list[a]
    list[a] = float(list[a])
print(list)