# 3.5


def fast_mul(x, y):
    res = 0
    if x % 2 == 1:
        res += y
    while x > 1:
        y *= 2
        x //= 2
        if x % 2 == 1:
            res += y
    return res


for i in range(100):
    for j in range(100):
        assert i * j == fast_mul(i, j)
