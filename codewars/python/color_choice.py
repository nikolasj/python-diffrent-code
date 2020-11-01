def checkchoose(m, n):
    r = 1
    for i in xrange(n + 1):
        if r == m: return i
        r = r * (n - i) / (i + 1)
    return -1


print(checkchoose(6, 4))
