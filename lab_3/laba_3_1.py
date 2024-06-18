from numpy import *


def input_mas(count):
    arr = empty(10, float)
    for i in range(count):
        arr[i] = float(input(f"Введите элемент {i + 1}: "))
    return arr


a = input_mas(10)
b = linspace(0, 9, 10)
c = random.randint(1, 5, size=10)

print("\nМассив a:")
print(a)
print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)

print("\nМассив b:")
print(b)
print(b.shape)
print(b.size)
print(b.ndim)
print(b.dtype)

print("\nМассив c:")
print(c)
print(c.shape)
print(c.size)
print(c.ndim)
print(c.dtype)

max_values = [max(a), max(b), max(c)]
average_max = mean(max_values)

print("\nМаксимальные значения: ", max_values)
print("Среднее арифметическое: ", average_max)

print("\na:", a)
print("b:", b)
print("Поэлементное перемножение массивов a и b: ", a * b)

print("\na:", a)
a = delete(a, [1, 3, 5])
print("Удаление 1, 3, 5 элемента из массива a: ", a)

print("\nb:", b)
print("Массив размера (2,3) из последних 6 элементов массива b:\n", b[-6:].reshape(2, 3))

d = copy(b)
print("\nb:", b)
print("Массив d, скопированный из b:", d)

print("\nc:", c)
print("d:", d)
d = concatenate((c, d))
print("Соединение массивов с и d:", d)
print("Массив d,  преобразованный в массив размера (4,5):\n", d.reshape(4, 5))

print("\nc:", c)
print("Массив c, в который дописали последовательность [2,4]:", append(c, [2, 4]))

print("\na:", a)
print("Сортировка массива a по возрастанию: ", sort(a))
print("\nb:", b)
print("Сортировка массива b по убыванию: ", flip(b))
