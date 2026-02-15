# 3.6


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


def fast_pow(x, y):
    res = 1
    for _ in range(y):
        res = fast_mul(res, x)
    return res


for i in range(50):
    for j in range(50):
        assert i**j == fast_pow(i, j)
