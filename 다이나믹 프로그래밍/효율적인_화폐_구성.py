import sys

sys.stdin = open("input.txt", "r")

def money_construction(n,m):

    dp_table = [10001] * (m+1)

    dp_table[0] = 0

    for i in range(n):
        for j in range(array[i], m+1):
            if dp_table[j-array[i]] != 10001:
                dp_table[j] = min(dp_table[j], dp_table[j-array[i]]+1)

    result = dp_table[m]

    return result

if __name__ == '__main__':
    
    N, M = map(int, sys.stdin.readline().split())

    array = []

    for _ in range(N):
        array.append(int(sys.stdin.readline()))

    print(money_construction(N,M))