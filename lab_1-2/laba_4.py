def input_mas(count):
    array = []
    for i in range(count):
        array.append(int(input(f"Введите элемент {i+1}: ")))
    return array


def input_matr(rows, columns):
    matr = []
    for i in range(rows):
        print(f"строка {i+1}:")
        matr.append(sorted(input_mas(columns)))

    return matr


def even_mas(array):
    new_array = []
    for i in array:
        if i % 2 == 0:
            new_array.append(i)
    if len(new_array) == 0:
        return "В массиве нет чётных чисел"
    return sorted(new_array)


print("Задание 1:")
N = int(input("Введите кол-во элементов массива: "))
mas = input_mas(N)
print(even_mas(mas))

print("\nЗадание 2:")
n = int(input("Введите кол-во строк массива: "))
m = int(input("Введите кол-во столбцов массива: "))
print(input_matr(n, m))
