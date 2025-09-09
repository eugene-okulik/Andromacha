a = 5

while True:
    user_input = int(input("Введите ваше число: "))
    if user_input == a:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
