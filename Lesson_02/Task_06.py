goods = []
features = {'название': '', 'цена': '', 'колличество': '', 'единица измерения': ''}
analitics = {'название':[], 'цена': [], 'колличество': [], 'единица измерения': []}
num = 0
while True:
    if input('Q - выход \n Любая клавиша продолжить: ').upper() == 'Q':
        break
    num += 1
    for i in features.keys():
        user_data = input('{}: '.format(f))
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitic[f].append(features[f])
    goods.append((num, features.copy()))
    print('текущая аналитика по товарам: \n')
    for key, value in analitics.items():
        print(key, value)
