import math
import heapq

def kClosest(points, k):
    
    heap, answer = [], []

    for point in points:
        x, y = point[0], point[1]
        distance = math.sqrt(x**2+y**2)
        heapq.heappush(heap,(distance, x,y))
    
    for _ in range(k):
        p = heapq.heappop(heap)
        answer.append([p[1], p[2]])

    return answer