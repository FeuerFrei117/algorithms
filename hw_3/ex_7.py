"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
"""

user_input = list(map(int, input('Введите массив целых чисел через пробел: ').split()))

# Вариант №1
min_num_one = user_input.pop(user_input.index(min(user_input)))

min_num_two = user_input.pop(user_input.index(min(user_input)))

print(f'Два наименьших элемента в массиве: {min_num_one}, {min_num_two}')

# Вариант №2
# min_num_one, min_num_two = user_input[1], user_input[0]
#
# for j in user_input:
#     if min_num_two > j:
#         min_num_two = j
# user_input.remove(min_num_two)
#
# for i in user_input:
#     if min_num_one > i:
#         min_num_one = i
#
# print(f'Два наименьших элемента в массиве: {min_num_one}, {min_num_two}')
