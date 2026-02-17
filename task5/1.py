from math import ceil


def main(y):
    n = len(y)
    result = 0

    for i in range(1, n + 1):
        result += 25 * (
            54 * y[ceil(i / 2) - 1] - y[n - i] ** 2 - y[ceil(i / 2) - 1] ** 3
        )

    return result
