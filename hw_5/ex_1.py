"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""

enterprises = {}
number_of_enterprises = int(input('Введите количество предприятий: '))

for i in range(number_of_enterprises):
    name_enterprises = input(f'Введите название предприятия №{i + 1}: ')
    profit_for_four_months = list(map(int, input('Введите через пробел прибыль за 4 квартала: ').split()))
    enterprises[name_enterprises] = profit_for_four_months

result = 0

for i in enterprises.values():
    result += sum(i)

print(f'\nСредняя прибыль за год всех предприятий составила: {"%.2f" % (result / number_of_enterprises)}')
print('Предприятия, чья прибыль выше среднего:')
for i in enterprises.keys():
    if sum(enterprises.get(i)) > (result / number_of_enterprises):
        print(f'{i}', end=', ')
print('\nПредприятия, чья прибыль ниже или равна среднему:')
for i in enterprises.keys():
    if sum(enterprises.get(i)) <= (result / number_of_enterprises):
        print(f'{i}', end=', ')
print()

for i in enterprises.keys():
    if enterprises.get(i)[0] > enterprises.get(i)[1] > enterprises.get(i)[2] > enterprises.get(i)[3]:
        print(f'{i} предприятие имеет строго убывающую последовательность прибыли')
    elif enterprises.get(i)[0] >= enterprises.get(i)[1] >= enterprises.get(i)[2] >= enterprises.get(i)[3]:
        print(f'{i} предприятие имеет не строго убывающую последовательность прибыли')
    elif enterprises.get(i)[0] < enterprises.get(i)[1] < enterprises.get(i)[2] < enterprises.get(i)[3]:
        print(f'{i} предприятие имеет строго возврастающую последовательность прибыли')
    elif enterprises.get(i)[0] <= enterprises.get(i)[1] <= enterprises.get(i)[2] <= enterprises.get(i)[3]:
        print(f'{i} предприятие имеет не строго возрастающую последовательность прибыли')
    elif ((enterprises.get(i)[0] <= enterprises.get(i)[1] >= enterprises.get(i)[2] >= enterprises.get(i)[3]) or
            (enterprises.get(i)[0] <= enterprises.get(i)[1] <= enterprises.get(i)[2] >= enterprises.get(i)[3])):
        print(f'{i} предприятие имеет возрастающе-убывающую последовательность прибыли')
    elif ((enterprises.get(i)[0] >= enterprises.get(i)[1] >= enterprises.get(i)[2] < enterprises.get(i)[3]) or
          (enterprises.get(i)[0] >= enterprises.get(i)[1] <= enterprises.get(i)[2] <= enterprises.get(i)[3])):
        print(f'{i} предприятие имеет убывающе-возрастающую последовательность прибыли')
    else:
        print(f'{i} предприятие имеет рандомную последовательность прибыли')
