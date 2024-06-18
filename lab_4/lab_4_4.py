import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')


def y5(x):
    return 2 * x ** 2 - x ** 3


# Диапазон значений
x = arange(-10, 10.1, 0.1)
z = x

# Создание трёхмерный осей
fig = plt.figure()
ax = plt.axes(projection='3d')

# Построение 3D линейного графика
ax.set_title('3D График')
ax.plot(x, y5(x), z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графика
plt.show()
