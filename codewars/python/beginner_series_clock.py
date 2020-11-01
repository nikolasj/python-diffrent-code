# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a?utm_source=newsletter

def past(h, m, s):
    return (h * 1000 * 60 * 60) + (m * 1000 * 60) + (s * 1000)


print(past(1, 0, 0))
