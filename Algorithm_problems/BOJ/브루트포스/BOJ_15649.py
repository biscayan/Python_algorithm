import sys
sys.stdin = open("input.txt", "r")

def dfs(result):
    if len(result) == M:
        for i in range(len(result)):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(result)
            visited[i] = False
            result.pop()

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    result = []
    visited = [False] * (N+1)
    dfs(result)