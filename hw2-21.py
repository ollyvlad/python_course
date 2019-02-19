from math import *

start_list = [2, -5, 8, 9, -25, 25, 4]
result = list()
for i in start_list:
   
    if i >= 0 and int(sqrt(i)) == sqrt(i):
 
        result.append(int(sqrt(i)))
print(result)   