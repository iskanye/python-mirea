import math


def main(x, y):
    return (
        math.asin(y - 1 - 78 * x**3) ** 2
        - (81 * y**3 + 1) ** 4
        + (
            ((14 * x**3 - 0.01 - y**2) ** 6 / 78)
            / (40 * (x**3 + y**2 / 7 + 19) ** 6 + math.sin(x) ** 4)
        )
        ** 0.5
    )
