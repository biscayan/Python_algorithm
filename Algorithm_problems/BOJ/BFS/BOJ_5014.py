import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs():
    queue = deque([S])
    visited[S] = 1
    while queue:
        x = queue.popleft()
        if x == G:
            print(visited[x]-1)
            return
        if x+U <= F and not visited[x+U]:
            visited[x+U] = visited[x] + 1
            queue.append(x+U)
        if x-D > 0 and not visited[x-D]:
            visited[x-D] = visited[x] + 1
            queue.append(x-D)
    print("use the stairs")

if __name__ == '__main__':
    F, S, G, U, D = map(int, sys.stdin.readline().split())
    visited = [0] * (F+1)
    bfs()