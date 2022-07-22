"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

user_input_one, user_input_two, user_input_three = list(input('Введите трехзначное число: '))
user_sum = int(user_input_one) + int(user_input_two) + int(user_input_three)
user_multiplication = int(user_input_one) * int(user_input_two) * int(user_input_three)
print(f'Сумма цифр трехзначного числа: {user_sum}\n'
      f'Произведение цифр трехзначного числа: {user_multiplication}')
