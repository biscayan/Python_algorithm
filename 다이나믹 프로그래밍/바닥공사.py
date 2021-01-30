import sys

sys.stdin = open("input.txt", "r")

def floor_construction(n):

    dp_table = [0] * n

    dp_table[0] = 1
    dp_table[1] = 3

    for i in range(2,n):
        dp_table[i] = (dp_table[i-2] * 2) + dp_table[i-1]

    result = dp_table[n-1] % 796796

    return result

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    print(floor_construction(N))