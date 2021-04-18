import sys

sys.stdin = open("input.txt", "r")

def min_max(num_list):

    num_list.sort()

    min_value = num_list[0]
    max_value = num_list[-1]

    return min_value, max_value


if __name__ =='__main__':
    N = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))

    a, b = min_max(nums)

    print(a,b)