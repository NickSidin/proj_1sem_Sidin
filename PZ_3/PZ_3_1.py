#Проверить истинность высказывания: "Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных".
import random #импорт из библиотеки random
A = random.randrange(-3,3)
B = random.randrange(-3,3)
C = random.randrange(-3,3)
print("A = ", A)
print("B = ", B)
print("C =", C)
ab = (A == -B)
bc = (B == -C)
ac = (A == -C)
x = ab or bc or ac
print("A противоположно B: ", ab)
print("B противоположно C:", bc)
print("A противоположно C:", ac)
print("Есть хотя бы одна пара взаимно противоположных", x)