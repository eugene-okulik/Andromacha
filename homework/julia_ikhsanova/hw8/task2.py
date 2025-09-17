import sys
sys.set_int_max_str_digits(0)

def gen(limit=100001):
    a = 0
    b = 1
    count = 0

    while count < limit:  # ограничиваем количеством
        yield a
        a, b = b, a + b
        count += 1

for i, g  in enumerate(gen()):
    if i in (5, 100, 1000, 100000): print(g)


    # if i == 5: print(g)
    # elif i == 200: print(g)
    # elif i == 1000: print(g)
    # elif i == 100000: print(g)

