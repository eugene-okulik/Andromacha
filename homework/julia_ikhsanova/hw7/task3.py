def process_line(line):
    print(int(line.split()[-1]) + 10)


lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
]

for line in lines:
    process_line(line)


# a = "результат операции: 42"
# qa = a.split()
# qaz = int(qa[-1])
# print(qaz + 10)
#
# b = "результат операции: 514"
# qb = int(b.split(":")[1])
# print(10 + qb)
#
# c = "результат работы программы: 9"
# qc = int(c.split(":")[1])
# print(10 + qc)
