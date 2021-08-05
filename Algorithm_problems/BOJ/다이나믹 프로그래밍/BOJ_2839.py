import sys

sys.stdin = open("input.txt", "r")

def deliver_sugar(N):

    if N == 3 or N == 5:
        return 1
    if N == 4 or N == 7:
        return -1

    INF = 1e9
    dp_table = [INF] * (N+1)
    dp_table[3], dp_table[5] = 1, 1

    for i in range(6, N+1):
        if dp_table[i-3] != INF:
            dp_table[i] = min(dp_table[i], dp_table[i-3]+1)
        if dp_table[i-5] != INF:
            dp_table[i] = min(dp_table[i], dp_table[i-5]+1) 

    return dp_table[N]

N = int(sys.stdin.readline())
print(deliver_sugar(N))