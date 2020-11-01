#  https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python

def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


print(capitalize("abcdef"))
