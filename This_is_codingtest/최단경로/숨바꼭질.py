import heapq
import sys

sys.stdin = open("input.txt", "r")

def hide_seek(start):

    heap = []
    heapq.heapify(heap)

    ### 힙에 (거리,노드) 튜플을 저장
    heapq.heappush(heap,(0,start))
    distance[start] = 0

    while heap:

        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for node in graph[now]:

            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(heap,(cost,node[0]))

    max_num = 0

    for i in range(1,N):
        if distance[i] > max_num:
            max_num = distance[i]
            barn_num = i+1
            barn_cnt = 1

        elif distance[i] == max_num:
            barn_cnt += 1

    print(barn_num, max_num, barn_cnt)


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    INF = 1e9

    graph = [[] for _ in range(N)]
    distance = [INF] * N

    for _ in range(M):
        barn1, barn2 = map(int, sys.stdin.readline().split())
        graph[barn1-1].append((barn2-1,1))
        graph[barn2-1].append((barn1-1,1))

    hide_seek(0)