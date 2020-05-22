from datetime import date

start = 1901
end = 2000
month = 12
print(sum(1 if date(y, m, 1).weekday() == 6 else 0 for m in range(1, month + 1) for y in range(start, end + 1)))
