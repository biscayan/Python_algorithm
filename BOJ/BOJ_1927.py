import sys
import heapq

sys.stdin = open("input.txt","r")

heap = []

### int(input())은 시간초과 발생

for _ in range(int(sys.stdin.readline())):

    x = int(sys.stdin.readline())
    
    ###x가 0이면 가장 작은 값을 출력
    if x == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))

        ###heap안에 요소가 없을때는 0을 출력
        else:
            print(0)
    else:
        heapq.heappush(heap,x)
