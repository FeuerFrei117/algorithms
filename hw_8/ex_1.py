"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только
из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def my_f(array):
    result = 1
    all_substrings = set()

    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            all_substrings.add(array[i:j])
    all_substrings.remove(array)
    all_substrings = list(all_substrings)
    for i in range(len(all_substrings)):
        if hashlib.sha1(all_substrings[-1].encode('utf-8')).hexdigest() != hashlib.sha1(all_substrings[i].encode
           ('utf-8')).hexdigest():
            result += 1

    return result


user_input = input('Введите строку без пробелов: ')

print(my_f(user_input))
