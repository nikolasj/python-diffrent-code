# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    res = 0
    for i in sentence:
        if i in ['a', 'e', 'i', 'o', 'u']:
            res += 1
    
    return res

print(get_count("aeiou"))
print(get_count("bcdfghjklmnpqrstvwxz y"))


# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")
