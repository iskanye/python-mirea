import math


def main(n):
    return (
        0.78
        if n == 0
        else (0.83 if n == 1 else math.sin(main(n - 2)) + main(n - 1) ** 3 / 89 + 0.05)
    )
