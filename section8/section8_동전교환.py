import sys

sys.stdin = open("input.txt", "r")

def Change_coin(array):

    dp_table = [M] * (M+1)
    dp_table[0] = 0

    for coin in array:
        for i in range(coin, M+1):
            dp_table[i] = min(dp_table[i],dp_table[i-coin] + 1)

    result = dp_table[M]

    print(result)

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    coin_list = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    Change_coin(coin_list)