from math import *

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = e ** ((b / a) ** 2) * abs(a ** 2 - b ** 2) ** (1 / 5) / (b * a ** (1 / 3) + a * (b ** (1 / 3))) - sin(a / b ** 2)

print("Результат:", round(c, 2))
