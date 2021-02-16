import sys

sys.stdin = open("input.txt", "r")

def coin_zero(array):

    global K

    count = 0

    idx = 0

    while True:

        if K == 0:
            print(count)
            break

        else:
            if array[idx] > K:
                idx += 1
            else:
                K -= array[idx]
                count += 1


if __name__ == '__main__':

    N, K = map(int, sys.stdin.readline().split())

    coin_list = []

    for _ in range(N):
        coin = int(sys.stdin.readline())
        coin_list.append(coin)
        if coin > K:
            break

    coin_list.sort(reverse=True)

    coin_zero(coin_list)