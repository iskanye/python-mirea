def main(m, a, n):
    return sum(
        (20 * j**3 + 61 + k) ** 2 / 12 - 24 * k
        for k in range(1, a + 1)
        for j in range(1, m + 1)
    ) + sum((j**7 - i**6 / 32 - 1) for i in range(1, n + 1) for j in range(1, m + 1))
