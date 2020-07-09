def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Введите число или q для выхода: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    print(result)

