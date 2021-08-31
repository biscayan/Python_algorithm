import sys
import heapq
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
left, right = [], []

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max heap
        heapq.heappush(left, -num)
    else:
        # min heap
        heapq.heappush(right, num)
    # swap
    if left and right and -left[0] > right[0]:
        left_value = -heapq.heappop(left)
        right_value = heapq.heappop(right)
        heapq.heappush(left, -right_value)
        heapq.heappush(right, left_value)

    print(-left[0])