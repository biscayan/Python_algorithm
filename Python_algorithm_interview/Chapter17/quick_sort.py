def quick_sort(array, low, high):
    def partition(low, high):
        pivot = array[high]
        left = low
        for right in range(low, high):
            if array[right] < pivot:
                array[left], array[right] = array[right], array[left]
                left += 1
        array[left], array[high] = array[high], array[left]
        return left

    if low < high:
        pivot = partition(low, high)
        quick_sort(array, low, pivot-1)
        quick_sort(array, pivot+1, high)

a = [1,5,2,7,3,4,8,6]
quick_sort(a, 0, len(a)-1)
print(a)