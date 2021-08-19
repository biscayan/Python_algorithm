import heapq

def findCheapestPrice(n, flights, src, dst, k) -> int:
    graph = [[] for _ in range(n)]
    for s,e,c in flights:
        graph[s].append((e,c))

    heap = []
    heapq.heappush(heap, (0,src,0))
    
    while heap:
        cost, cur, edge = heapq.heappop(heap)
        if cur == dst:
            return cost
        if edge <= k:
            for v,w in graph[cur]:
                total = w+cost
                heapq.heappush(heap, (total,v,edge+1))

    return -1