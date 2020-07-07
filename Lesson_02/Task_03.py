# вариант 1

seasons_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: "Summer",
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter',
}

month = int(input('Введите месяц'))
if month <= 0 or month >= 13:
    print('Нет такого месяца')
else:
    print(seasons_dict[month])

# вариант 2

seasons_list = [' ',
    'Winter',
    'Winter',
    'Spring',
    'Spring',
    'Spring',
    "Summer",
    'Summer',
    'Summer',
    'Autumn',
    'Autumn',
    'Autumn',
    'Winter'
]

month = int(input('Введите месяц'))
if month <= 0 or month >= 13:
    print('Нет такого месяца')
else:
    print(seasons_list[month])