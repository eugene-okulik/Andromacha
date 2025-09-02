import math


class HW_Task4:
    # Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

    a = 100
    b = 10

    def hypotenuse(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def area(self):
        return 0.5 * self.a * self.b


new = HW_Task4()

v = new.hypotenuse()
print(v)
f = new.area()
print(f)
