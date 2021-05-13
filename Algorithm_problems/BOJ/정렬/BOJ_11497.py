import sys
import heapq

sys.stdin = open("input.txt", "r")

def jump_log(array):

    heapq.heapify(array)

    sorted_array = [0] * N

    ### location : 좌우 판별 (0이면 좌, 1이면 우)
    location, idx = 0, 0

    while array:    

        min_num = heapq.heappop(array)

        ### 좌 우 한번씩 최소값을 입력
        if location == 0:
            sorted_array[idx] = min_num
            location = 1 - location

        elif location == 1:
            sorted_array[N-1-idx] = min_num
            location = 1 - location
            idx += 1

    answer = 0

    for i in range(N):
        answer = max(answer, abs(sorted_array[i] - sorted_array[i-1]))

    print(answer)
        

if __name__ == '__main__':

    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        array = list(map(int, sys.stdin.readline().split()))
        jump_log(array)