# Задача 14: 

# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Enter border number N: '))

num = 2
i = 0
result = 0
while result <= N:
    result = num ** i
    i += 1
    if result <= N:
        print(result, end=' ')

