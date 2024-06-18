import matplotlib
import matplotlib.pyplot as plt
from numpy import *

matplotlib.use('TkAgg')


def y1(x):
    return 2 * x ** 2


def y2(x):
    return 5 * x + 4


# Диапазон значений x
x = arange(-5, 6, 1)

# Размер фигуры
plt.figure(figsize=(5, 5))

# Построение графика y1 в виде линии (цвет жёлтый, тип линии '--', толщина 1.5)
plt.plot(x, y1(x), label='y1', linestyle='--', color='gold', linewidth='1.5')

# Построение графика y2 в виде точек (цвет красный, тип маркера '*')
plt.scatter(x, y2(x), label='y2', marker='*', color='red')

# Легенда
plt.legend()

# Заголовок
plt.title('Графики функций y1 и y2', fontsize='16', color='black')

# Оси
plt.xlabel('x')
plt.ylabel('y')

# Сетка
plt.grid(True)

# Установка явных значений на оси x с шагом 1
plt.xticks(arange(-5, 6, 1))

# Отображение графика
plt.show()
