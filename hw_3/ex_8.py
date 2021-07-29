"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

length, number_columns = map(int, input('Введите длину и количество столбцов матрицы через пробел: ').split())

matrix = []

for i in range(number_columns):
    matrix.append(list(map(int, input(f'Введите {length} символов для {i + 1} строки: ').split())))
    # matrix[i].append(sum(matrix[i]))   # зависит какой сценарий необходим

for i in matrix:
    for j in i:
        print("%3d" % j, end=' ')
    print('   |', sum(i))   # зависит какой сценарий необходим
    # print()  # зависит какой сценарий необходим

for i in range(length):
    print('---', end=' ')
print()

for i in range(length):
    max_num = 0
    for j in range(number_columns):
        if matrix[j][i] > max_num:
            max_num = matrix[j][i]
    print("%3d" % max_num, end=' ')
