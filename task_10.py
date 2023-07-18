# Задача 10:

# На столе лежат n монеток. Некоторые из них лежат
# вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той 
# же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

from random import randint

n = int(input("Enter the number of coins: "))

eagle_counter = 0
tails_counter = 0
for _ in range(n):
    droping = randint(0, 1)
    print(droping)
    if droping == 0:
        tails_counter += 1
    elif droping == 1:
        eagle_counter += 1
print('Coins with tails: ', tails_counter)
print('Coins with eagle: ', eagle_counter)

if tails_counter < eagle_counter:
    print('There are fewer tails, it is easier to flip coins with tails')
elif tails_counter > eagle_counter:
    print('There are fewer eagle, it is easier to flip coins with eagle')
else:
    print('Coins with eagle and tails are equal, you can flip any of them')




