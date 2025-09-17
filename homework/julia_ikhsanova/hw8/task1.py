import random

salary = int(input("Enter salary: "))
bonus = random.choice([True, False])

result = salary
if bonus:
    result += int(random.random() * 5000) + 1  # от 1 до 5000

print(f"{salary}, {bonus} - '${result}'")
