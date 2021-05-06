import sys

sys.stdin = open("input.txt", "r")

def sum_twonum(nums):

    count = 0

    nums.sort()

    ### two pointers
    start, end = 0, len(nums)-1
    
    while start < end:
        if nums[start] + nums[end] < x:
            start += 1
        elif nums[start] + nums[end] > x:
            end -= 1
        elif nums[start] + nums[end] == x:
            count += 1
            end -= 1

    return count


if __name__ == '__main__':

    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline())

    print(sum_twonum(num_list))