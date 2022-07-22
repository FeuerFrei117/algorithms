"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def reverse_list(lst):
    rev = []
    for i in lst:
        rev.append(i)
    rev.reverse()
    return rev


def list_to_string(lst):
    s = ''
    for i in lst:
        s += i
    return s.upper()


def hex_to_dec(hex_lst):
    base = 16
    dec = 0
    trans_hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    for i in range(len(hex_lst)):
        dec += trans_hex_dict[hex_lst[i]] * base ** i
    return dec


def dec_to_hex(dec):
    base = 16
    trans_dec_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    hex_list = []
    while dec > 0:
        hex_list += [trans_dec_dict[dec % base]]
        dec //= base
    return hex_list


hex1 = list(input('Введите первое шестнадцатиричное число: ').upper())
hex2 = list(input('Введите второе шестнадцатиричное число: ').upper())

print(f'Массив первого числа: {hex1}\nМассив втого числа: {hex2}')

hex1_rev = reverse_list(hex1)
hex2_rev = reverse_list(hex2)

dec1 = hex_to_dec(hex1_rev)
dec2 = hex_to_dec(hex2_rev)
print(f'В DEC СИСТЕМЕ:\nпервое число: {dec1}\nвторое число: {dec2}')

sum_dec = dec1 + dec2
multiplication_dec = dec1 * dec2
print(f'сумма: {sum_dec}\nпроизведение: {multiplication_dec}')

sum_hex = reverse_list(dec_to_hex(sum_dec))
multiplication_hex = reverse_list(dec_to_hex(multiplication_dec))

print(f'В HEX СИСТЕМЕ:\nсумма: {list_to_string(sum_hex)}')
print(f'произведение: {list_to_string(multiplication_hex)}')

sum_hex_list = list(map(str, (i for i in sum_hex)))
multiplication_hex_list = list(map(str, (i for i in multiplication_hex)))

print(f'Сумма чисел из листа {sum_hex_list}\nПроизведение чисел из листа {multiplication_hex_list}')
