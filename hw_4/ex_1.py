"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.

Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, то надо вывести число 6843.
"""
import cProfile
import timeit


# Решение №1
def ver_one(num):
    j = ''
    for i in num:
        j += num[len(num) - int(i)]
    return j


# Решение №2
def ver_two(num):
    j = ''
    for i in num[::-1]:
        j += i
    return j


# Решение №3
def ver_three(num):
    if len(num) == 1:
        return num[-1]
    else:
        return num[-1] + ver_three(num[:-1])


print(cProfile.run('ver_one("123" * 10000)'))
print(cProfile.run('ver_two("123" * 10000)'))
print(cProfile.run('ver_three("123" * 100)'))
print()

print(timeit.timeit('ver_one("123")', 'from __main__ import ver_one'))
print(timeit.timeit('ver_two("123")', 'from __main__ import ver_two'))
print(timeit.timeit('ver_three("123")', 'from __main__ import ver_three'))
print()

"""
* не совсем понимаю как работать с "cProfile". При его вызове возвращается статистика работы функций, но не
прописывается сколько времени занимает выполнение каждой строки.

* при использовании "timeit" мы видим среднее время выполнение функции. Как и было сказано на уроке и в методичке
на работу со списком уходит гораздо меньше времени (затрачивается меньше вычислительной мощности компьютера). ЧТД.
"""