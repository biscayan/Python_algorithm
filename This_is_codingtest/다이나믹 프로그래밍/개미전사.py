import sys

sys.stdin = open("input.txt", "r")

def ant_warrior(n, array):

    dp_table = [0] * n

    dp_table[0] = array[0]
    dp_table[1] = max(array[0], array[1])

    for i in range(2, n):
        dp_table[i] = max(dp_table[i-1], dp_table[i-2]+array[i])

    result = dp_table[n-1]

    return result

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    food_storage = list(map(int, sys.stdin.readline().split()))

    print(ant_warrior(N, food_storage))