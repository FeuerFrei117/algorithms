"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""

input_year = int(input('Введите год: '))

if input_year % 2 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print('Год високосный')
        else:
            print('Год не високосный')
    else:
        print('Год високосный')
else:
    print('Год не високосный')
