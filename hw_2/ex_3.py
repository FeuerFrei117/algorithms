"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, то надо вывести число 6843.
"""

# user_input = input('Введите число: ')

# Решение №1
# for i in user_input:
#     print(user_input[len(user_input) - int(i)], end='')

# Решение №2
# for i in user_input[::-1]:
#     print(i, end='')


# Решение №3
def reverse_num(num):
    if len(num) == 1:
        return num[-1]
    else:
        return num[-1] + reverse_num(num[:-1])


print(reverse_num(str(input('Введите число: '))))
