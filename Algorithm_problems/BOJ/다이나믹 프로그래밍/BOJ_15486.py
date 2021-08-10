import sys

sys.stdin = open("input.txt", "r")

def resignation(N):
    dp_table = [0] * (N+1)
    max_profit = 0
    for i in range(N-1,-1,-1):
        ti, pi = array[i]
        if ti+i <= N:
            dp_table[i] = max(dp_table[ti+i]+pi, max_profit)
            max_profit = dp_table[i]
        else:
            dp_table[i] = max_profit
    return max_profit

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    array = []
    for _ in range(N):
        Ti, Pi = map(int, sys.stdin.readline().split())
        array.append((Ti,Pi))
    print(resignation(N))