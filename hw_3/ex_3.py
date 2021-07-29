"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

user_input = list(map(int, input('Введите через пробел массив случайных целых чисел: ').split()))

print(user_input)

num_min, num_max = user_input[0], user_input[0]

for i in user_input:
    if i > num_max:
        num_max = i
    if num_min > i:
        num_min = i

user_input[user_input.index(num_max)], user_input[user_input.index(num_min)] = \
    user_input[user_input.index(num_min)], user_input[user_input.index(num_max)]

print(user_input)
