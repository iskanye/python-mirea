def main(n):
    binary = bin(n)[2:].zfill(32)
    Y1 = int(binary[31:32], 2)
    Y2 = int(binary[25:31], 2)
    Y3 = int(binary[15:25], 2)
    Y4 = int(binary[7:15], 2)
    return (hex(Y1), hex(Y2), hex(Y3), hex(Y4))


print(main(13439869))
print(main(21759412))
print(main(6123164))
print(main(31221119))