"""
Определить, какое число в массиве встречается чаще всего.
"""

user_input = list(map(int, input('Введите массив чисел через пробел: ').split()))

count, max_nam = 0, 0

# Вариант №1
for i in set(user_input):
    if user_input.count(i) > count:
        count = user_input.count(i)
        max_nam = i

# Вариант №2
# for i in set(user_input):
#     j = 0
#     for t in user_input:
#         if t == i:
#             j += 1
#     if j > count:
#         count = user_input.count(i)
#         max_nam = i

print(f'Число {max_nam} в массиве встречается {count} раз')
