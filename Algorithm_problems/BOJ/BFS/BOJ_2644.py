import sys
from collections import deque

sys.stdin = open("input.txt","r")

def bfs(v):

    queue = deque()
    queue.append(v)

    visited = [False] * (n+1)

    answer = 0

    while queue:

        answer += 1

        for _ in range(len(queue)):

            person = queue.popleft()

            if person == b:
                return answer -1

            for i in array[person]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
    
    return -1

if __name__ == '__main__':
    ###사람의 수
    n = int(sys.stdin.readline())

    ###찾고자 하는 촌수의 대상들
    a, b = map(int, sys.stdin.readline().split())

    ###부모자식 관계 수
    m = int(sys.stdin.readline())

    array = [[] for _ in range(n+1)]

    for _ in range(m):
        ###부모자식의 쌍
        x, y = map(int, sys.stdin.readline().split())

        ###부모자식의 관계
        array[x].append(y)
        array[y].append(x)

    print(bfs(a))