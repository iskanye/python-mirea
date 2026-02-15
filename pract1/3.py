# 3.7


def mul_bits(x, y, bits):
    x &= 2**bits - 1
    y &= 2**bits - 1
    return x * y


def mul16(x, y):
    mask = 2**8 - 1
    x1 = x & mask
    x2 = x >> 8
    y1 = y & mask
    y2 = y >> 8

    m_11 = mul_bits(x1, y1, 8)
    m_12 = mul_bits(x1, y2, 8)
    m_21 = mul_bits(x2, y1, 8)
    m_22 = mul_bits(x2, y2, 8)

    result = m_11 + (m_12 << 8) + (m_21 << 8) + (m_22 << 16)
    return result


for i in range(1024):
    for j in range(1024):
        assert i * j == mul16(i, j)
