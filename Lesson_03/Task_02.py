def personal_info(**kwargs):
    return kwargs
print(personal_info(
    name=input('Имя: ') ,
    surname=input('Фамилия: '),
    britday=input('Дата рождения: '),
    city=input('Город: '),
    email=input('Почта: '),
    phone=input('Телефон: '),

))
