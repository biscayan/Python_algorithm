import heapq
import sys

sys.stdin = open("input.txt", "r")

def assign_room(classes):

    ### 힙에는 끝나는 시간이 저장됨
    heap = [classes[0][1]]
    heapq.heapify(heap)

    for i in range(1, N):

        end_time = heap[0]

        ### 이전 수업의 끝나는 시간과 현재 수업의 시작시간을 비교
        if classes[i][0] < end_time:
            heapq.heappush(heap,classes[i][1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap,classes[i][1])

    answer = len(heap)

    return answer


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    classes = []

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        classes.append((start, end))

    classes.sort(key = lambda x:x[0])
    
    print(assign_room(classes))