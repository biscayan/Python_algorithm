import sys
import heapq

sys.stdin = open("input.txt", "r")

def lec_tour(univ_list):
    
    heap = []

    for univ in univ_list:
        heapq.heappush(heap, univ[1])
        # delete the univ which gives the lowest payment
        if len(heap) > univ[0]:
            heapq.heappop(heap)

    return sum(heap)

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    univ_list = []

    for _ in range(n):
        p, d = map(int, sys.stdin.readline().split())
        univ_list.append((d,p))
        
    univ_list.sort()

    print(lec_tour(univ_list))