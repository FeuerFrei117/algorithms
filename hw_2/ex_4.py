"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

# цикл и рекурсия

user_input = input('Введите ряд чисел через пробел: ').split()
sum_number = 0

for i in user_input:
    sum_number += float(i)

print(f'Сумма введенного Вами ряда чисел ровна {sum_number}')


def sum_num(num):
    if len(num) == 1:
        return float(user_input.pop(0))
    else:
        return float(user_input.pop(0)) + float(sum_num(num))


print(sum_num(user_input))
