def binary_search(array, target, start, end):

    while start <= end:
        
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        elif array[mid] < target:
            start = mid + 1

    return None


if __name__ == '__main__':

    target = 7

    array = [1,3,5,7,9,11,13,15,17,19]

    result = binary_search(array, target, 0, len(array)-1)

    print(target,"은",result+1,"번째 자리에 있습니다.")