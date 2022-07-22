"""
Написать два алгоритма нахождения i-го по счёту простого числа.

Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
в виде комментариев в файле с кодом.
"""
import cProfile
import timeit


# Используя алгоритм «Решето Эратосфена»
def ver_1(n):
    num_list = list(range(int(n)))

    num_list[1] = 0

    for i in num_list:
        if i > 1:
            for j in range(i + i, len(num_list), i):
                num_list[j] = 0

    num_list = set(num_list)

    num_list.remove(0)

    return num_list


# Без использования «Решета Эратосфена»
def ver_2(n):
    lst = [2]
    for i in range(3, int(n), 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(ver_1(23))
print(ver_2(23))

print(cProfile.run('ver_1("23")'))
print(cProfile.run('ver_2("23")'))

print(timeit.timeit('ver_1("230")', 'from __main__ import ver_1'))
print(timeit.timeit('ver_2("230")', 'from __main__ import ver_2'))

"""
Время выполнения алгоритма №1 = 60 сек
Время выполнения алгоритма №2 = 90 сек

Вывод: выбор алгоритма решения поставленной задачи важная часть программирования. Нужно выбирать оптимальное решение и 
учиться писать сразу качественный код. Если какие - то процессы проходят медленно разбираться в причинах с помощью
необходимых модулей и оптимизировать код.
"""
