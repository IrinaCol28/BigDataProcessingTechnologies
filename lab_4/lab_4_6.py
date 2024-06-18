import matplotlib
import matplotlib.pyplot as plt
from numpy import *

matplotlib.use('TkAgg')

# Создание двумерного массива
random_array = random.uniform(0, 1, size=(10, 10))

# Размеры рисунка и отступы подграфиков
fig, axs = plt.subplots(2, 2, figsize=(9, 9))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Первый рисунок (просто массив в виде изображения)
fig.colorbar(axs[0, 0].imshow(random_array))
axs[0, 0].set_title('Исходный массив', fontsize='14', color='black')

# Второй рисунок (срез центра 4х4)
fig.colorbar(axs[0, 1].imshow(random_array[3:7, 3:7]))
axs[0, 1].set_title('Центральная часть 4х4', fontsize='14', color='black')

# Третий рисунок (инвертирование)
fig.colorbar(axs[1, 0].imshow(1 - random_array))
axs[1, 0].set_title('Инвертированный массив', fontsize='14', color='black')


# Создание нового массива для размытого изображения
blurred_array = copy(random_array)
rows, cols = random_array.shape

# Проходим по каждой строке (кроме крайних)
for i in range(rows):
    for j in range(1, cols - 1):
        blurred_array[i, j] = (random_array[i, j - 1] + random_array[i, j] + random_array[i, j + 1]) / 3

# Четвёртый рисунок (размытие)
fig.colorbar(axs[1, 1].imshow(blurred_array))
axs[1, 1].set_title('Размытый массив', fontsize='14', color='black')


plt.show()

# Сохранение в файл
fig.savefig('Изображение.jpeg')
