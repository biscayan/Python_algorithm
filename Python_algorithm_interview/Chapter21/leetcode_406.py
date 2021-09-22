import heapq

def reconstructQueue(people):
    heap, answer = [], []
    for h,k in people:
        heapq.heappush(heap,(-h, k))
    while heap:
        person = heapq.heappop(heap)
        answer.insert(person[1], [-person[0], person[1]])
    return answer