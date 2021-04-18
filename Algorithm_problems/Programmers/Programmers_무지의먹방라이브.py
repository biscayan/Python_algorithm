import heapq

def solution(food_times,k):

    if sum(food_times)<=k:
        return -1

    heap = []

    ###먹는데 시간이 적게 소요되는 순서로 heappush
    for i in range(len(food_times)):
        heapq.heappush(heap,(food_times[i],i+1))
    
    eat_time = 0
    pre_time = 0

    food_nums = len(food_times)

    while eat_time + ((heap[0][0]-pre_time)*food_nums) <= k:

        min_time = heapq.heappop(heap)[0]

        ###최소 시간의 음식을 다 먹는데 걸린 시간을 더함
        eat_time += (min_time-pre_time)*food_nums
        
        ###음식 하나를 다 먹었으므로 개수를 줄임
        food_nums -= 1

        pre_time = min_time

    ###음식 번호 순서로 정렬
    after_error = sorted(heap, key = lambda x:x[1])

    result = after_error[(k-eat_time)%food_nums][1]

    return result


if __name__ == '__main__':
    food_times = [3,1,2]
    k = 5

    print(solution(food_times, k))