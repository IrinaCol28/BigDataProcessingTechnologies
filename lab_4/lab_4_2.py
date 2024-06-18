import matplotlib
import matplotlib.pyplot as plt
from numpy import *

matplotlib.use('TkAgg')


def y1(x):
    return abs(2 * x)


def y2(x):
    return 2 * abs(x)


def y3(x):
    return abs(2 + x)


def y4(x):
    return -x ** 3


def y5(x):
    return 2 * x ** 2 - x ** 3


def y6(x):
    return 3 - x ** 3

# Диапазон значений x
x = arange(-10, 10.1, 0.1)

# Размер 1 рисунка
fig1 = plt.figure(figsize=(13, 5))

# Задаем 1 подграфик 1 рисунка
plt.subplot(1, 3, 1)
plt.plot(x, y1(x), '-r', linewidth='1.5')
plt.title('График функции y1', fontsize='16', color='black')
plt.grid(True)

# Задаем 2 подграфик 1 рисунка
plt.subplot(1, 3, 2)
plt.plot(x, y2(x), '--g', linewidth='1.5')
plt.title('График функции y2', fontsize='16', color='black')
plt.grid(True)

# Задаем 3 подграфик 1 рисунка
plt.subplot(1, 3, 3)
plt.plot(x, y3(x), '-.b', linewidth='1.5')
plt.title('График функции y3', fontsize='16', color='black')
plt.grid(True)

# Размер 2 рисунка
fig2 = plt.figure(figsize=(13, 5))

# Задаем 1 подграфик 2 рисунка
plt.subplot(1, 3, 1)
plt.plot(x, y4(x), '--y', linewidth='1.5')
plt.title('График функций y4', fontsize='16', color='black')
plt.grid(True)

# Задаем 2 подграфик 2 рисунка
plt.subplot(1, 3, 2)
plt.plot(x, y5(x), '-.k', linewidth='1.5')
plt.title('График функции y5', fontsize='16', color='black')
plt.grid(True)

# Задаем 3 подграфик 2 рисунка
plt.subplot(1, 3, 3)
plt.plot(x, y6(x), '-.m', linewidth='1.5')
plt.title('График функции y6', fontsize='16', color='black')
plt.grid(True)

# Отображение рисунков с графиками
plt.show()
