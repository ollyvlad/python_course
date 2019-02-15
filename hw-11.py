print('ДЗ-1, задача 1')

getnumber = int(input('Введите целое число больше одной цифры'))

while getnumber != 0:
            digit = getnumber % 10
            print(digit)
            getnumber = getnumber // 10