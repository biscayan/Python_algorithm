import sys

sys.stdin = open("input.txt", "r")

def common_bag(items):
    
    dp_table = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # knapsack algorithm
    for i in range(1, N+1):
        for j in range(1, K+1):
            weight, value = items[i][0], items[i][1]
            # can't contain the item
            if weight > j:
                dp_table[i][j] = dp_table[i-1][j]
            # can contain the item
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-weight]+value)

    return dp_table[N][K]

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    item_list = [(0,0)]
    for _ in range(N):
        W, V = map(int, sys.stdin.readline().split())
        item_list.append((W,V))
    print(common_bag(item_list))