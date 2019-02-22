def filtered_lst(a, b):
    final_list = list()
    for x in b:
        if a(x) == True:
            final_list.append(x)
        else:
            continue
    return final_list
 
 
print((filtered_lst((lambda x: x > 8), b=[1, 2, 65, 4, 6, 5, 3, 0, 1245])))