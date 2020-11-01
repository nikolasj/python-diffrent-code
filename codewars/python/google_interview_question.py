# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python


def get_strings(s):
    return ','.join(f"{i}:{'*' * s.lower().count(i)}" for i in dict.fromkeys(s.replace(' ', '').lower()))


print(get_strings("Las Vegas"))
