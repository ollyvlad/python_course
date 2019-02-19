from random import randint
user_num = input('Введите количество элементов списка')
result = [randint(-100, 100) for i in range(int(user_num))]
print(result)