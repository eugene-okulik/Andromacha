def repeat_me(func):

    def wrapper(text, count):
        func(text)
        for i in range(count):
            print(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', 0)


# def repeat_me(count=1):               # сюда попадает число повторений
#     def decorator(func):              # сюда попадает функция example
#         def wrapper(*args, **kwargs): # это "обёртка", которая запускает функцию
#             for _ in range(count):    # повторяем count раз
#                 func(*args, **kwargs)
#         return wrapper                # возвращаем обёртку
#     return decorator                  # возвращаем декоратор
#
# @repeat_me(count=2)                   # указываем, сколько раз повторять
# def example(text):
#     print(text)
#
# example("print me")