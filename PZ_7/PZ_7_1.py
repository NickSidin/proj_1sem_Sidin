# Дано целое положительное число.
# Вывести символы, изображающие цифры этого числа (в порядке слева направо).
try:
    number = int(input('Введите число: '))
    list_1 = list(str(number))
    print('Начальное число: ', number)
    print('Cимволы, к-рые изображают цифры этого числа (слева направо): ', *list_1[::+1], sep= ' ')
except ValueError:
    print('Неверно')
