import sys
import heapq

sys.stdin = open("input.txt","r")

heap = []

while True:

    element = int(input())

    if element == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(heapq.heappop(heap))
    
    elif element == -1:
        break

    else:
        heapq.heappush(heap,element)
