
def my_num(num_1, num_2,):
    try:
        mun_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'ошибка числа'
    except ZeroDivisionError:
        return 'на ноль делить нельзя'
    return answer

print(my_num(
    num_1=input('введите чило 1: '),
    num_2=input('введите число 2: '),
))
