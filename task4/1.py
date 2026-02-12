import math


def main(n):
    if n == 0:
        return 0.78
    if n == 1:
        return 0.83
    return math.sin(main(n - 2)) + main(n - 1) ** 3 / 89 + 0.05
