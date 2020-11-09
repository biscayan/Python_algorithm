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
            ### -를 붙여 원래의 값을 출력
            print(-heapq.heappop(heap))
    
    elif element == -1:
        break

    else:
        ### -를 붙여서 정렬순서를 뒤바꿈
        heapq.heappush(heap,-element)