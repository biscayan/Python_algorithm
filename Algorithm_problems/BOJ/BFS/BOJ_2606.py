import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(one):

    queue = deque([])

    queue.append(one)

    while queue:

        virus = queue.popleft()

        if 1 not in infected[virus]:
            ### 감염된 컴퓨터 체크
            infected[virus].append(1)
            for com in network[virus]:
                queue.append(com)
    

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    relation = int(sys.stdin.readline())

    network = [[] for _ in range(n+1)]
    infected = [[0] for _ in range(n+1)]

    for _ in range(relation):

        com1, com2 = map(int, sys.stdin.readline().split())

        network[com1].append(com2)
        network[com2].append(com1)

    ### 1번 컴퓨터가 바이러스에 걸림
    bfs(1)

    answer = 0

    ### 2번 컴퓨터부터 감염여부확인
    for i in range(2,n+1):
        answer += sum(infected[i])

    print(answer)