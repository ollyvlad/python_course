
def sort_to_max(list_):
    a = 1
    while a < len(list_):
        for i in range(len(list_)-a):
            if list_[i] > list_[i+1]:
                list_[i],list_[i+1] = list_[i+1],list_[i]
        a += 1
    return list_
result = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(result)