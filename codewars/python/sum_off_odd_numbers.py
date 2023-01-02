# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

# def row_sum_odd_numbers(n):
#     first_hundred_odd = list(range(1, 2000, 2))
#     result = []
#     flag = False
#     for i in range(1, n + 1):
#         if n == i:
#             if i % 2 == 0:
#                 flag = True
#             for j in range(i, i + i):
#                 if flag:
#                     result.append(first_hundred_odd[j - 1])
#                 else:
#                     result.append(first_hundred_odd[j])
#
#     return sum(result)

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3

print(row_sum_odd_numbers(13))

"""
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
"""