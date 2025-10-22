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
