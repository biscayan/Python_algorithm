import sys
sys.stdin = open("input.txt", "r")

def dfs(lvl, num_sum):
    global answer
    if num_sum == S:
        answer += 1
    for j in range(lvl+1, N):
        dfs(j, num_sum+array[j])

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(0,N):
        dfs(i, array[i])
    print(answer)