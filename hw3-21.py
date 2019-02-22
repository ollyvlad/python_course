def fibonacci(n, m):
    """
   :n: начальное число
   :m: конечное число в ряду
   :return: ряд чисел от n до m
   """
    a, b = 1, 1
    fib_lst = [1, ]
 
    for i in range(m):
        a, b = b, a + b
        fib_lst.append(a)
 
    return fib_lst[n - 1:m]
 
 
print('Ряд Фибоначчи с 1 до 18', fibonacci(1, 18))