class HW_Task2:
    # Даны числа x и y. Получить x − y / 1 + xy

    a = 100
    b = 2

    def addition(self):
        c = self.a - (self.b / (1 + self.a * self.b))
        print(c)

new = HW_Task2()

new.addition()
