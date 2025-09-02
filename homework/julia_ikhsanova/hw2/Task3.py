class HW_Task3:
    # Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

    a = 100
    b = 10

    def addition(self):
        c=(self.a + self.b)/2
        print(c)

    def geometric_mean(self):
        l=(self.a * self.b)/2
        print(l)



new = HW_Task3()
new.addition()
new.geometric_mean()
