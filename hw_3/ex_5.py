"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

user_input = list(map(int, input('Введите массив чисел через пробел: ').split()))

position, min_nam = 0, 0

for i in set(user_input):
    if min_nam > i:
        min_nam = i
        position = user_input.index(i) + 1

print(f'Максимальный отрицательный элемент: {min_nam}; его позиния в массиве: {position}')
