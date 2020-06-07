# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python

def expression_matter(a, b, c):
    result = []
    result.append(a * (b + c))
    result.append(a * b * c)
    result.append(a + b * c)
    result.append(a + b + c)
    result.append((a + b) * c)

    return max(result)


print(expression_matter(1, 1, 1))

# return max(a + b + c, (a + b) * c, a * (b + c), a * b * c)
