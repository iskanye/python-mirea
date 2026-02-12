from math import ceil


def main(y):
    n = len(y)

    return sum(
        25 * (54 * y[ceil(i / 2) - 1] - y[n - i] ** 2 - y[ceil(i / 2) - 1] ** 3)
        for i in range(1, n + 1)
    )
