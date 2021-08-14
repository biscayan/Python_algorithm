def hammingDistance(x: int, y: int) -> int:
    xor = bin(x ^ y)
    return xor.count('1')