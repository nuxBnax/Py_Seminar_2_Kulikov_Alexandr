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
first_number = (sum + (sum ** 2 - 4 * prod) ** 0.5) / 2
second_number = (sum - (sum ** 2 - 4 * prod) ** 0.5) / 2
print(first_number, second_number )