# вариант 1

def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans
print(my_pow_func(10, -2))

# вариант 2

def my_pow_func(x, y):
    try:
        x,y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x
        return 1 / res
    except ValueError:
        return 'Check value'
print(my_pow_func(10, -2))