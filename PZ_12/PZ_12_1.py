# Вариант №20.
# В последовательности на N целых элементов в первой ее половине найти количество положительных элементов.
# import random

lst = [-1, 2, -3, 4, 5, 6, -7, 8, -9, 10]
print(f'Последовательность: {lst}')
plus = [n for n in lst[0:len(lst)//2] if n>=0]
print(f'Количество положительных чисел в первой половине: {len(plus)}')