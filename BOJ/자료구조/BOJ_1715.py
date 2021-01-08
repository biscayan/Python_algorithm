import sys
import heapq

sys.stdin = open("input.txt", "r")

def sort_card(heap):

    count = 0

    while heap:
        
        ### 카드 묶음이 한 개이면 더 비교할 수 없으므로 return
        if len(heap) == 1:
            return count

        else:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)

            ### 두 개의 카드 묶음을 합침 
            num_sum = num1 + num2

            count += num_sum
            
            heapq.heappush(heap, num_sum)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    heap = []

    for _ in range(N):

        num = int(sys.stdin.readline())

        ### 최소힙
        heapq.heappush(heap, num)

    print(sort_card(heap))