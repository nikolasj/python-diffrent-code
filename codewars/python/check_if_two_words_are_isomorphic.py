# https://www.codewars.com/kata/59dbab4d7997cb350000007f/train/python

# def isomorph(a, b):
#     result_a = {}
#     count_b = {}
#
#     if len(a) != len(b):
#         return False
#
#     for i in range(len(a)):
#         result_a[a[i]] = {"letter": b[i], "count": 0}
#
#     for i in range(len(a)):
#         if b[i] != result_a[a[i]]:
#             return False
#
#     # for i in range(len(b)):
#     #     if b[i] == result[a[i]]:
#     #         continue
#     #     else:
#     #         return False
#
#     return True


# from collections import Counter
#
#
# def isomorph(a, b):
#     if len(Counter(a)) != len(Counter(b)) or len(a) != len(b):
#         return False
#
#     lookup = {}
#     for letter, morph in zip(a, b):
#         if letter in lookup and lookup[letter] != morph:
#             return False
#         lookup[letter] = morph
#
#     return True

from collections import defaultdict


def isomorph(a, b):
    print(a, b)
    da, db = defaultdict(list), defaultdict(list)
    for i in range(len(a) == len(b) and len(a)):
        print(da)
        print(db)
        if da[a[i]] != db[b[i]]:
            print('t')
            return False
        da[a[i]].append(i)
        db[b[i]].append(i)
    return bool(da)


# print(isomorph('RAMBUNCTIOUSLY', 'THERMODYNAMICS'))

print(isomorph('AB', 'CC'))
