import heapq
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

heap = list(map(int, sys.stdin.readline().split()))
heapq.heapify(heap)

for _ in range(N-1):

    array = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        heapq.heappush(heap, array[i])
        heapq.heappop(heap)

print(heap[0])


'''
메모리 초과

import heapq
import sys

def find_N(array):

    ### 마지막 줄의 요소들의 값으로 heap를 초기화
    heap = [array[N-1][i] for i in range(N)]
    heapq.heapify(heap)

    for i in range(N-2,-1,-1):
        for j in range(N):

            ### 현재 힙의 최소값
            min_num = heap[0]
        
            if array[i][j] > min_num:
                heapq.heappush(heap, array[i][j])
                heapq.heappop(heap)
            else:
                return min_num


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    array = [sorted(list(map(int, sys.stdin.readline().split())), reverse=True) for _ in range(N)]

    print(find_N(array))
'''