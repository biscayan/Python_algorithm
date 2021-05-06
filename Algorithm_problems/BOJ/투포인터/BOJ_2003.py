import sys

sys.stdin = open("input.txt", "r")

def num_sum(nums):

    count = 0

    ### two pointers
    start, end = 0, 0

    while start < N and end < N:

        if sum(nums[start:end+1]) < M:
            end += 1
        elif sum(nums[start:end+1]) > M:
            start += 1
        elif sum(nums[start:end+1]) == M:
            count += 1
            end += 1

    return count


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))

    print(num_sum(num_list))