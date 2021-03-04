import sys

sys.stdin = open("input.txt", "r")

def tiling(n):

    if n == 1:
        return 1
        
    dp_table = [0] * n

    dp_table[0] = 1
    dp_table[1] = 2

    for i in range(2,n):
        dp_table[i] = dp_table[i-2] + dp_table[i-1]

    result = dp_table[n-1] % 10007

    return result


if __name__ == '__main__':

    n = int(sys.stdin.readline())

    print(tiling(n))