# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    str_ = ""
    for i in string_:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            continue
        str_ += i 
    return str_

print(disemvowel("This website is for losers LOL!"))


# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")