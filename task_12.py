# Задача 12:

# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две 
# подсказки. Он называет сумму этих чисел S и их 
# произведение P. Помогите Кате отгадать задуманные 
# Петей числа.


sum = int(input('Enter Sum of two numbers: '))
prod = int(input('Enter Product of two numbers: '))

if sum > 2000 or sum <= 0 or prod > 1000000 or sum == 1 or prod == 0:
        print('Error! Numbers X and Y must be from 1 to 1000')
else:   
    x = (sum + (sum ** 2 - 4 * prod) ** 0.5) / 2
    y = (sum - (sum ** 2 - 4 * prod) ** 0.5) / 2
    print('number X: ', x)
    print('number Y: ', y)