fruits = ['слива', 'груша', 'киви', 'яблоко', 'манго']
for fruit in fruits:
    print(str(fruits.index(fruit)+1) + ') ' + '{:>1}'.format(fruit))	