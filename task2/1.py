import math


def main(y):
    if y < -26:
        return math.log2(y**3 / 43) ** 6 / 54 - y**6 / 39
    elif -26 <= y < 71:
        return 20 + 60 * math.ceil(y**3 - 1) ** 6
    elif 71 <= y < 171:
        return y**7 / 67 + 30 * (65 * y**2) ** 6
    else:
        return 92 + y**4
