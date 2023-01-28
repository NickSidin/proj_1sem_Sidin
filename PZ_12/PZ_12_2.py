# Вариант №20. Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string.
# "In PyCharm, you can specify third-party standalone applications and run them as External Tools"

import string

str = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
symb = [' ', '-', '.', ':', ';','"']
lst = [n for n in str if n in string.ascii_lowercase
       or n in symb]
print(''.join(lst))