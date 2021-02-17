import heapq

def min_heap_sort(array):
    
    heap = []
    sorted_array = []

    for num in array:
        heapq.heappush(heap, num)

    for _ in range(len(heap)):
        sorted_array.append(heapq.heappop(heap))

    for item in sorted_array:
        print(item, end = ' ')
    print()


def max_heap_sort(array):
    
    heap = []
    sorted_array = []

    for num in array:
        heapq.heappush(heap, -num)

    for _ in range(len(heap)):
        sorted_array.append(-heapq.heappop(heap))

    for item in sorted_array:
        print(item, end = ' ')
    print()


if __name__ == '__main__':

    array = [1,3,5,7,9,2,4,6,8,0]

    min_heap_sort(array) # 0 1 2 6 3 5 4 7 8 9
    max_heap_sort(array) # 9 8 7 6 5 4 3 2 1 0
