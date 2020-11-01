# https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python

import re


def hydrate(drink_string):
    sum_alc = 0
    for i in drink_string.split(","):
        temp = re.findall('(\d+)', i)
        for j in temp:
            sum_alc += int(j)

    if sum_alc > 1:
        return "{} glasses of water".format(sum_alc)
    else:
        return "{} glass of water".format(sum_alc)


print(hydrate("1 chainsaw and 2 pools"))

# def hydrate(drink_string):
#     c=sum(int(c) for c in drink_string if c.isdigit())
#     return "{} {} of water".format(c,'glass') if c==1 else "{} {} of water".format(c,'glasses')
