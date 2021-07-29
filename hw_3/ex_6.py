"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и
максимальный элементы в сумму не включать.
"""

user_input = list(map(int, input('Введите массив чисел через пробел: ').split()))

min_num, max_num = user_input[0], user_input[0]

for i in set(user_input):
    if i > max_num:
        max_num = i
    if min_num > i:
        min_num = i

sum_num = user_input[user_input.index(min_num) - 1] + user_input[user_input.index(min_num) + 1 - len(user_input)] +\
      user_input[user_input.index(max_num) - 1] + user_input[user_input.index(max_num) + 1 - len(user_input)]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum_num}')
