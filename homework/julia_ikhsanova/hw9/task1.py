from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"

dt = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

print(dt.strftime("%B"))   # January

print(dt.strftime("%d.%m.%Y, %H:%M"))






