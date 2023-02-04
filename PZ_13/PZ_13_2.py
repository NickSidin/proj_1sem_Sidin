#Вариант №20. В матрице найти минимальный и максимальный элементы.

from random import randint
stroki = int(input('Количество строк в матрице: '))
stolbec = int(input('Количество столбцов в матрице: '))
mat = [[randint(0, 100) for i in range(stolbec)] for i in range(stroki)]
print(f"Дана матрица: ")

for i in mat:
    print(str(i))

up = [max(i) for i in mat]
down = [min(i) for i in mat]
print(f"Максимальный элемент матрицы: {max(up)}\nМинимальный элемент матрицы: {min(down)}")