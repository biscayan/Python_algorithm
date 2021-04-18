import sys

sys.stdin = open("input.txt", "r")

def count_num(array, target_num):

    left = find_left(array, target_num, 0, N-1)
    right = find_right(array, target_num, 0, N-1)

    if left == None:
        count = 0
        return count

    count = right-left+1

    return count

def find_left(array, target ,start, end):

    while start<=end:
        
        mid = (start+end)//2

        if (mid == 0 or target > array[mid-1]) and array[mid] == target:
            return mid

        ### 왼쪽만 탐색
        elif array[mid] >= target:
            end = mid-1
        
        ### 오른쪽만 탐색
        elif array[mid] < target:
            start = mid+1


def find_right(array, target ,start, end):

    while start<=end:
        
        mid = (start+end)//2

        if (mid == N-1 or target < array[mid+1]) and array[mid] == target:
            return mid

        ### 왼쪽만 탐색
        elif array[mid] > target:
            end = mid-1
            
        ### 오른쪽만 탐색
        elif array[mid] <= target:
            start = mid+1

if __name__ == '__main__':

    N, x = map(int,sys.stdin.readline().split())
    num_list = list(map(int,sys.stdin.readline().split()))

    result = count_num(num_list, x)

    print(result)