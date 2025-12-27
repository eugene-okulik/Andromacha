from datetime import datetime, timedelta


file_path = "/Users/juliaikhsanova/PycharmProjects/Andromacha/homework/eugene_okulik/hw_13/data.txt"

date_formats = [
    '%Y-%m-%d %H:%M:%S.%f',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d',
    '%Y',
]


def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        try:
            number_part, rest = line.split('.', 1)
            number = int(number_part.strip())
        except ValueError:
            print(f"Неверный формат строки: {line}")
            continue


        date_part = rest.strip().split(' -')[0]
        date_obj = parse_date(date_part)

        if not date_obj:
            print(f"Не удалось распознать дату: '{date_part}'")
            continue

        if number == 1:
            new_date = date_obj + timedelta(days=7)
            print(new_date)

        elif number == 2:
            day_of_week = date_obj.strftime('%A')
            print(day_of_week)

        elif number == 3:
            now = datetime.now()
            days_ago = (now - date_obj).days
            print(days_ago)