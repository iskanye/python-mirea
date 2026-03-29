def main(n):
    Y1 = (n >> 0) & ((1 << 1) - 1)
    Y2 = (n >> 1) & ((1 << 6) - 1)
    Y3 = (n >> 7) & ((1 << 10) - 1)
    Y4 = (n >> 17) & ((1 << 8) - 1)
    return (hex(Y1), hex(Y2), hex(Y3), hex(Y4))


print(main(13439869))
print(main(21759412))
print(main(6123164))
print(main(31221119))