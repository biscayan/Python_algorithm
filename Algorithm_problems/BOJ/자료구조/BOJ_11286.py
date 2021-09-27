import sys
import heapq
sys.stdin = open("input.txt", "r")

minus, plus = [], []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(plus, num)
    elif num < 0:
        heapq.heappush(minus, -num)
    else:
        if not minus and not plus:
            print(0)
        elif not minus and plus:
            print(heapq.heappop(plus))
        elif minus and not plus:
            print(-heapq.heappop(minus))
        else:
            p, m = plus[0], minus[0]
            if p < m:
                print(p)
                heapq.heappop(plus)
            else:
                print(-m)
                heapq.heappop(minus)