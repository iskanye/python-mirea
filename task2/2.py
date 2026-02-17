import math


def main(y):
    return (
        math.log2(y**3 / 43) ** 6 / 54 - y**6 / 39
        if y < -26
        else (
            20 + 60 * math.ceil(y**3 - 1) ** 6
            if -26 <= y < 71
            else (y**7 / 67 + 30 * (65 * y**2) ** 6 if 71 <= y < 171 else 92 + y**4)
        )
    )
