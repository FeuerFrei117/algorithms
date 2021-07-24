"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его
цифр.
"""

user_input = input('Введите через пробел любое колличество натуральных чисел: ').split()

max_num, max_num_sum = 0, 0

for i in user_input:
    sum_num = 0
    for n in range(len(i)):
        sum_num += int(i[n])
    if sum_num > max_num_sum:
        max_num, max_num_sum = i, sum_num

print(f'Число с наибольшей суммой цифр: {max_num}\n'
      f'Сумма его цифр: {max_num_sum}')
