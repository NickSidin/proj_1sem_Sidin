#Даны два числа. Вывести вначале большее, а затем меньшее из них.
import random

A = random.randrange(-3,3)
B = random.randrange(-3,3)
print("Два числа:", A, B)

if A > B:
    print (A,B)
else:
    print(B,A)