import numpy as np

#Сформировать два двумерных массива а и b размера (4,4)

#Массив a ввести с клавиатуры
a = np.empty((4, 4), dtype=int)
for i in range(4):
    a[i] = list(map(int, input(f"Введите {i+1}-ю строку массива а: ").split()))

#Массив b заполнить любыми числами
b = np.random.randint(-10, 10, size=(4, 4))

# Вывести на экран каждый массив и его атрибуты (shape, size, ndim, dtype)
print("Массив a:")
print(a)
print("Атрибуты массива a:")
print("Shape:", a.shape)
print("Size:", a.size)
print("Ndim:", a.ndim)
print("Dtype:", a.dtype)

print("\nМассив b:")
print(b)
print("Атрибуты массива b:")
print("Shape:", b.shape)
print("Size:", b.size)
print("Ndim:", b.ndim)
print("Dtype:", b.dtype)

# сформировать и вывести на экран центральную часть 2x2 массива a;
central_part_a = a[1:3, 1:3]
print("\nЦентральная часть 2x2 массива 'a':")
print(central_part_a)

# вычислить произведение массивов a и b
product_ab = np.multiply(a, b)
print("\nПроизведение массивов 'a' и 'b':")
print(product_ab)

# в массиве a заменить вторую строку суммой первой и третьей строк (сумма вычисляется поэлементно)
a[1] = np.sum(a[[0, 2]], axis=0)
print("\nМассив а: (заменить вторую строку суммой первой и третьей строк):")
print(a)

# Вставьте новый столбец в массив 'b' между вторым и третьим столбцами
new_column = np.random.randint(-10, 10, size=(4, 1))
b = np.insert(b, 2, new_column, axis=1)
print("\nМассив b: (новый столбец между вторым и третьим столбцами):")
print(b)

# Соедините массивы 'a' и 'b' по вертикали
c = np.hstack((a, b))
print("\nМассив 'c' (соединение массивов 'a' и 'b' по вертикали):")
print(c)

# Измените размер массива 'c' на (2, 16) - обрежем до 2 строки и 16 столбцов
c = c[:2, :16]
print("\nИзмененный размер массива 'c' (2x16):")
print(c)

# Удалите 2, 3, 4 столбцы массива 'c'
c = np.delete(c, [2, 3, 4], axis=1)
print("\nМассив 'c' после удаления 2, 3, 4 столбцов:")
print(c)

# Сформируйте одномерный массив из 1 и 2 строки массива 'a'
one_dimensional_array = a[0:2].flatten()
print("\nОдномерный массив из 1 и 2 строки массива 'a':")
print(one_dimensional_array)
