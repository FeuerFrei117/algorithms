"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""

import sys


# Lesson 1, ex_1
# @profile
def l1_ex1():
    user_input_one, user_input_two, user_input_three = list(input('Введите трехзначное число: '))
    user_sum = int(user_input_one) + int(user_input_two) + int(user_input_three)
    user_multiplication = int(user_input_one) * int(user_input_two) * int(user_input_three)
    total_bit = sys.getsizeof(user_input_one) + sys.getsizeof(user_input_two) + sys.getsizeof(user_input_three) +\
        sys.getsizeof(user_sum) + sys.getsizeof(user_multiplication)
    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')
    return (f'Сумма цифр трехзначного числа: {user_sum}\n'
            f'Произведение цифр трехзначного числа: {user_multiplication}')


# l1_ex1()


# Lesson 1, ex_2
# @profile
def l1_ex2():
    print(~5, ~6)
    print('*' * 50)
    print(5 << 2)
    print(5 >> 2)
    print(6 << 2)
    print(6 >> 2)
    print('*' * 50)
    print(5 & 6)
    print('*' * 50)
    print(5 ^ 6)
    print('*' * 50)
    print(5 | 6)
    total_bit = sys.getsizeof(~5, ~6) + sys.getsizeof(5 << 2) + sys.getsizeof(5 >> 2) + sys.getsizeof(6 << 2) +\
        sys.getsizeof(6 >> 2) + sys.getsizeof(5 & 6) + sys.getsizeof(5 ^ 6) + sys.getsizeof(5 | 6)
    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


# l1_ex2()


# Lesson 1, ex_3
# @profile
def l1_ex3():
    x_1, y_1 = input('Введите координаты точки 1: ').split()
    x_2, y_2 = input('Введите координаты точки 2: ').split()

    k = (float(y_1) - float(y_2)) / (float(x_1) - float(x_2))
    b = float(y_2) - k * float(x_2)

    total_bit = sys.getsizeof(x_1) + sys.getsizeof(x_2) + sys.getsizeof(y_1) + sys.getsizeof(y_2) +\
        sys.getsizeof(k) + sys.getsizeof(b)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')

    print(f'y = {k:.2f} * x + {b:.2f}')


# l1_ex3()


# Lesson 2, ex_1
# @profile
def l2_ex1():
    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))
    operations = input('Введите необходимое действие ("+", "-", "*", "/"): ')

    if operations == '+':
        print(number_one + number_two)
    elif operations == '-':
        print(number_one + number_two)
    elif operations == '*':
        print(number_one * number_two)
    elif operations == '/':
        if number_two == 0:
            print('Делить на "0" нельзя!')
        else:
            print(number_one / number_two)
    else:
        print('Вы ввели что-то не то')

    total_bit = sys.getsizeof(number_one) + sys.getsizeof(number_two) + sys.getsizeof(operations)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


# l2_ex1()


# Lesson 2, ex_2
# @profile
def l2_ex2():
    user_input = input('Введите натуральное число: ')
    even = 0
    odd = 0

    for i in user_input:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'У вашего числа четных чисел: {even};\n'
          f'не четных чисел: {odd}')

    total_bit = sys.getsizeof(user_input) + sys.getsizeof(even) + sys.getsizeof(odd)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


# l2_ex2()


# Lesson 2, ex_3
# @profile
def l2_ex3():
    user_input = input('Введите число: ')
    for i in user_input[::-1]:
        print(i, end='')

    print(f'\nВыделено {sys.getsizeof(user_input)} байт под переменные и 20 MB потрачено на скрипт')


# l2_ex3()


# Lesson 3, ex_1
# @profile
def l3_ex1():
    for i in range(2, 10):
        count = 0
        for j in range(2, 100):
            if j % i == 0:
                count += 1
        print(f'Числу {i} кратно {count} чисел ')

    # тут переменные находятся в цикле был ли смысл их считать
    total_bit = sys.getsizeof(i) + sys.getsizeof(j) + sys.getsizeof(count)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


# l3_ex1()

# Lesson 3, ex_2
# @profile
def l3_ex2():
    user_input = input('Введите массив чисел через пробел с запятой: ').split(', ')

    result = []

    for i in user_input:
        if int(i) % 2 == 0:
            result.append(user_input.index(i) + 1)

    print(f'В этих позициях первого массива стоят четные числа: {result}')

    total_bit = sys.getsizeof(user_input) + sys.getsizeof(result)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


# l3_ex2()


# Lesson 3, ex_3
# @profile
def l3_ex3():
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

    total_bit = sys.getsizeof(user_input) + sys.getsizeof(num_min) + sys.getsizeof(num_max)

    print(f'Выделено {total_bit} байт под переменные и 20 MB потрачено на скрипт')


l3_ex3()

"""
Вывод: чем меньше переменных, тем меньше будет затрачено памяти. Но при этом всегда выделяется 20Mb на скрипт, но если
необходимо, будет выделена дополнительная память.
"""
