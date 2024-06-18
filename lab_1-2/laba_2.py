from math import *

x = float(input("Введите x: "))

if x < -3:
    y = 7 * sqrt(abs(x - 1)) - 11
elif -3 <= x < 3:
    y = x
else:
    y = 7 * sqrt(abs(x + 1)) + 11

print("y равен: ", y)
