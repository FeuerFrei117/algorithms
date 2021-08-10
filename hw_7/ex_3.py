"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random

# random.seed(17)


# самый простой способ
def my_f_one(new_list):
    median = sorted(new_list)[len(new_list) // 2]
    return median


# пузырьковая сортировка
def my_f_two(new_list):
    n = 1
    while n < len(new_list):
        for i in range(len(new_list) - n):
            if new_list[i] < new_list[i + 1]:
                new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        n += 1
    median = new_list[len(new_list) // 2]
    return median


# сортировка расческой
def my_f_three(new_list):
    step = int(len(new_list) // 1.247)
    while step >= 1:
        for i in range(len(new_list) - step):
            if new_list[i] > new_list[i + step]:
                new_list[i], new_list[i + step] = new_list[i + step], new_list[i]
        step = int(step // 1.247)
    median = new_list[len(new_list) // 2]
    return median


# сортировка вставками
def my_f_four(new_list):
    for i in range(len(new_list)):
        num = new_list[i]
        count = i
        while (new_list[count - 1] > num) and count > 0:
            new_list[count] = new_list[count - 1]
            count = count - 1
        new_list[count] = num
    median = new_list[len(new_list) // 2]
    return median


user_input = int(input('Введите натуральное число: '))
my_list = list(random.randint(1, 2 * user_input + 1) for i in range(2 * user_input + 1))


print(my_list)
print(f'Результат решения №1: {my_f_one(my_list)}')
print(f'Результат решения №2: {my_f_two(my_list)}')
print(f'Результат решения №3: {my_f_three(my_list)}')
print(f'Результат решения №4: {my_f_four(my_list)}')
