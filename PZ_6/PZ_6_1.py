#Дан список размера N и целые числа K и L (1 < K < L < N).
#Найти среднееарифметическое элементов списка с номерами от Kдо L включительно.
import random
n = input('Введите размер списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input('Это не число! Попробуйте снова: ')
if n == 1:
    print('Среднее арифметическое элементов списка с номерами от K до L включительно: ', 1)
elif n == 2:
    print('Среднее арифметическое элементов списка с номерами от K до L включительно: ', 2)
elif n > 2 :
    N = []
    for x in range(n):
        N.append(random.randint(1, n))
        L = random.randrange(1, n)
while L == 1:
    L = random.randrange(1, n)
K = random.randrange(1, L)
summa = 0
i = 0
for x in N:
    if K <= x <= L:
        summa += x
        i+=1
else:
    ...
print('Среднее арифметическое элементов списка с номерами от K до L включительно: ', summa/i)