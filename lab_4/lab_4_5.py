import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')

# Диапазон значений
x = arange(-3, 17, 0.4)
y = arange(1, 6, 0.1)
xgrid, ygrid = meshgrid(x, y)
zgrid = xgrid + 1 / (2 * ygrid)

# Создание трёхмерный осей
fig = plt.figure()
ax = plt.axes(projection='3d')

# Создаем 3D поверхность
surf = ax.plot_surface(xgrid, ygrid, zgrid, cmap='plasma')

# Добавляем цветовую шкалу
fig.colorbar(surf)

# Добавления названия осей и графика
ax.set_title('3D Поверхность')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение поаерхности
plt.show()
