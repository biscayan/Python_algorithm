def quick_sort(array, start, end):

    if start >= end:
        return 

    pivot = start

    left = start + 1
    right = end

    while left <= right:

        ### 왼쪽에서 피벗보다 큰 데이터를 찾고
        while left <= end and array[pivot] >= array[left]:
            left += 1
 
        ### 오른쪽에서 피벗보다 작은 데이터를 칮음
        while right > start and array[pivot] <= array[right]:
            right -= 1

        ### 두 개의 탐색이 엇갈렸다면
        if left > right:
            ### pivot의 데이터를 값이 더 작은 right의 데이터와 바꿈
            array[pivot], array[right] = array[right], array[pivot]

        else:
            array[left], array[right] = array[right], array[left]

    ### 피벗의 왼쪽 리스트와 오른쪽 리스트를 재귀적으로 분할하며 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


if __name__ == '__main__':

    array = [5,3,6,7,2,8,0,4,9,1]
    
    quick_sort(array, 0, len(array)-1)

    print(array)