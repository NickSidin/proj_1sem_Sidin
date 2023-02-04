#Вариант №20. В матрице найти сумму элементов первых двух строк.

from random import randint
stroki = int(input('Количество строк в матрице: '))
stolbec = int(input('Количество столбцов в матрице: '))
mat = [[randint(0, 50) for i in range(stolbec)] for i in range(stroki)]
print(f"Дана матрица: ")

for i in mat:
    print(str(i))

double = [i for i in mat[:2][:]]
print(f"Первые две строки матрицы: {double}")
plus = [sum(i) for i in double[:][:]]
print(f'Сумма элементов первых двух строк матрицы: {sum(plus)}')