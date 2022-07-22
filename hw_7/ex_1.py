"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""
import copy
import random
# random.seed(17)


# пузырьковая сортировка
def my_f_one(new_list):
    n = 1
    while n < len(new_list):
        for i in range(len(new_list) - n):
            if new_list[i] < new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        n += 1
    return new_list


# сортировка расчёской
def my_f_two(new_list):
    step = int(len(new_list) // 1.247)
    while step >= 1:
        for i in range(len(new_list) - step):
            if new_list[i] < new_list[i + step]:
                new_list[i], new_list[i + step] = new_list[i + step], new_list[i]
        step = int(step // 1.247)
    return new_list


my_list = list(range(-100, 100))

random.shuffle(my_list)

print(f'Неотсортированный массив:\n{my_list}')

print(f'Пузырьковая сортировка:\n{my_f_one(copy.copy(my_list))}')

print(f'Сортировка расчёсткой:\n{my_f_two(copy.copy(my_list))}')
