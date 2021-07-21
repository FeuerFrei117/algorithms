"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

one_symbol, two_symbol = input('Ведите две буквы, через пробел: ').split()
one_symbol = ord(one_symbol) - 96
two_symbol = ord(two_symbol) - 96
letters_between = two_symbol - one_symbol - 1
print(f'Первая буква стоит на {one_symbol} месте в алфавите\n'
      f'Вторая буква стоит на {two_symbol} месте в алфавите\n'
      f'Между ними находится {letters_between} букв')

