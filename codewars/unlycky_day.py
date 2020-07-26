# https://www.codewars.com/kata/56eb0be52caf798c630013c0/train/python
from datetime import date

def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))


print(unlucky_days(2015))
