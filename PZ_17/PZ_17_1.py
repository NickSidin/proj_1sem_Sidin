# Вариант 20. Cоздайте класс "Счётчик", который имеет
# атрибут текущего значения и методы для инкремента и декремента значения.

class Counter:
    def __init__(self, number):
        self.number = number

    def increment_number(self, new_number):
        self.number += new_number
        return f"Значение после прибавления new_number: {self.number}"

    def dicrement_number(self, new_number):
        self.number -= new_number
        return f"Значение после вычитания new_number: {self.number}"


obj = Counter(30)
obj_2 = Counter(10)
print(obj.increment_number(3))
print(obj.dicrement_number(10))
print()
print(obj_2.increment_number(4))
print(obj_2.dicrement_number(10))