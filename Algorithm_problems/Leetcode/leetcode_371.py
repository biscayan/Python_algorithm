def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MASK = 0X7FFFFFFF

    a_bin = bin(a&MASK)[2:].zfill(32)
    b_bin = bin(b&MASK)[2:].zfill(32)

    result = []
    carry, bit_sum = 0,0

    for i in range(32):
        A = int(a_bin[31-i])
        B = int(b_bin[31-i])

        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        bit_sum = carry ^ Q2
        carry = Q1 | Q3

        result.append(str(bit_sum))

    if carry == 1:
        result.append('1')

    result = int(''.join(result[::-1]), 2) & MASK

    if result > INT_MASK:
        result = ~(result ^ MASK)

    return result

# simple code
def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MASK = 0X7FFFFFFF

    while b!= 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a> INT_MASK:
        a = ~(a ^ MASK)

    return a