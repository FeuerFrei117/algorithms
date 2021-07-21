"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

num_one, num_two, num_three = input('Введите через пробел три числа: ').split()

if int(num_one) > int(num_two):
    if int(num_two) > int(num_three):
        print(f'Средним числом является: {num_two}')
    else:
        if int(num_one) > int(num_three):
            print(f'Средним числом является: {num_three}')
        else:
            print(f'Средним числом является: {num_one}')
else:
    if int(num_two) < int(num_three):
        print(f'Средним числом является: {num_two}')
    else:
        if int(num_one) > int(num_three):
            print(f'Средним числом является: {num_one}')
        else:
            print(f'Средним числом является: {num_three}')
