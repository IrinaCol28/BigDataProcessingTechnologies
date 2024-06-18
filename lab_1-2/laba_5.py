from math import *
from tabulate import tabulate


def math_function(x):
    return -x ** (1 / 2) * sin(x ** 2 / 100)


def golden_ratio(a, b, e):
    counter = 1
    Fi = 1.618033988749
    x_0 = a
    x_3 = b
    x_1 = b - (x_3 - x_0) / Fi
    x_2 = x_0 + x_3 - x_1
    data = []
    while True:
        f_1 = math_function(x_1)
        f_2 = math_function(x_2)
        data.append([counter, x_0, x_3, x_3 - x_0, x_1, x_2, f_1, f_2])
        if f_1 < f_2:
            I = x_2 - x_0
            x_3 = x_2
            x_2 = x_1
            x_1 = x_0 + I / Fi
        else:
            I = x_3 - x_1
            x_0 = x_1
            x_1 = x_2
            x_2 = x_0 + I / Fi
        counter += 1
        if I < e:
            break
    headers = ["N", "x0", "x3", "x3-x0", "x1", "x2", "f1", "f2"]
    table = tabulate(data, headers, tablefmt="grid", floatfmt=(".6f", ".6f", ".6f", ".6f", ".6f", ".6f", ".6f", ".6f"))
    print(table)
    print(f"Минимум функции: {math_function(x_1)}, при х: {x_1}")


a = float(input("Введите a: "))
b = float(input("Введите b: "))
e = float(input("Введите точность: "))
golden_ratio(a, b, e)
