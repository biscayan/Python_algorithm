def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array