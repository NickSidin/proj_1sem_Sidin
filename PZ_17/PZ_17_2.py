# Вариант 20. Cоздание базового класса "Работник" и его наследование
# для создания классов "Менеджер" и "Инженер". В классе "Работник" будут
# общие методы, такие как "работать" и "получать зарплату", а классы-наследники
# будут иметь свои уникальные методы и свойства, такие как
# "управлять командой" и "проектировать системы".


class WorkMan:
    def work(self, do: True or False):
        self.worked = do
        return f"Работают: {self.worked}"

    def get_zarplat(self, zr: True or False):
        self.take_zarplat = zr
        return f"Получают зарплату: {self.take_zarplat}"


class Manager(WorkMan):
    def __init__(self, zarplata):
        self.zarplata = zarplata
        self.otdel = "Менеджер"

    def manage_command(self, manage: True or False):
        self.manage = manage
        return f"Управление командой: {self.manage}"

    def project_system(self, ans: True or False):
        self.yprav = ans
        return f"Проектирование системы: {self.yprav}"

class Injener(WorkMan):
    def __init__(self, zarplata):
        self.zarplata = zarplata
        self.otdel = 'Инженер'


    def manage_command(self, manage: True or False):
        self.manage = manage
        return f"Управление командой: {self.manage}"

    def project_system(self, ans: True or False):
        self.yprav = ans
        return f"Проектирование системы: {self.yprav}"

Man_1 = Manager(19000)
Man_2 = Injener(40000)
print(Man_1.manage_command(True))
print(Man_1.project_system(False))
print(Man_1.get_zarplat(True))
print(Man_1.work(True))

print()

print(Man_2.manage_command(False))
print(Man_2.project_system(False))
print(Man_2.get_zarplat(True))
print(Man_2.work(True))