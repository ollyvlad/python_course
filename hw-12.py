print('ДЗ-1, задача 1.2')

first_var = input('Напишите сюда слово или число ')
second_var = input('А сюда еще какое-то слово или число ')

first_var, second_var = second_var, first_var


store_var = first_var
first_var = second_var
second_var = store_var
print(second_var, "Теперь это первое")
print(first_var, "Теперь это второе")
