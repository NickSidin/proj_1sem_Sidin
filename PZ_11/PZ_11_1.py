# Вариант 20. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из
# целых положительных и отрицательных чисел.
# сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трём:
# Количество чисел кратных трём:

numbers = ['-1 21 34 6 7 -3 -52 -9']

f1 = open('info.txt', 'w')
f1.writelines(numbers)
f1.close()

f2 = open('info_copy.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(numbers)
f2.close()

f1 = open('info.txt') # Вычисляем количество элементов, числа кратные трём и количество чисел кратных трём
k = f1.read()
k = k.split()
crat = []
for i in range(len(k)):
    k[i] = int(k[i])
    if k[i] % 3 == 0:
        crat.append(k[i])
crat_count = len(crat)
f1.close()

f1 = open('info.txt') # Вычисляем минимальный элемент
min, t = 0, 0
for i in range(len(k)):
    min = min if min < k[i] else k[i]
    if k[i] < 0:
        t += 1
f1.close()

f2 = open('info_copy.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(k), '\n', 'Минимальный элемент: ', min, '\n', 'Числа кратные трём: ', crat,
      '\n', 'Количество чисел кратных трём: ', crat_count, file=f2)
f2.close()

f1 = open('info.txt')
f2 = open('info_copy.txt')
print('Первый файл: ', '\n', f1.read())
print('Второй файл: ', '\n', f2.read())
f1.close()
f2.close()