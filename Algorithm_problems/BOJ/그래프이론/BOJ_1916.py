import sys
import heapq

sys.stdin = open("input.txt", "r")

def get_min_cost(start, final):

    distance = [1e9] * (N+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (start, distance[start]))

    while heap:
        cur, cost = heapq.heappop(heap)
        # go to the same city, but it requires more cost
        if distance[cur] < cost:
            continue
        for nxt in graph[cur]:
            if distance[nxt[0]] > cost+nxt[1]:
                distance[nxt[0]] = cost+nxt[1]
                heapq.heappush(heap,(nxt[0], distance[nxt[0]]))
                
    print(distance[final])

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        s, d, c = map(int, sys.stdin.readline().split())
        graph[s].append((d,c))

    start, final = map(int, sys.stdin.readline().split())

    get_min_cost(start, final)