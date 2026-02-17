def main(m, a, n):
    result = 0
    for k in range(1, a + 1):
        for j in range(1, m + 1):
            result += (20 * j**3 + 61 + k) ** 2 / 12 - 24 * k
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result += j**7 - i**6 / 32 - 1
    return result
