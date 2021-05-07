import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

def topology_sort():

    result = copy.deepcopy(time)

    queue = deque()

    ### 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:

        node = queue.popleft()

        for i in graph[node]:
            result[i] = max(result[i], result[node] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in range(1, N+1):
        print(result[i])


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    time = [0] * (N+1)

    for i in range(1,N+1):
        data = list(map(int, sys.stdin.readline().split()))
        time[i] = data[0]
        for x in data[1:-1]:
            indegree[i] += 1
            graph[x].append(i)

    topology_sort()