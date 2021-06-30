import sys

sys.stdin = open("input.txt", "r")

def immigration(left, right):

    while left <= right:

        mid = (left+right) // 2
        num_sum = 0

        for i in range(N):
            num_sum += mid // num_list[i]

        if num_sum >= M:
            right = mid - 1
            answer = mid

        else:
            left = mid + 1

    print(answer)

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())
    num_list = list()

    min_num, max_num = 100001, 0

    for _ in range(N):
        num = int(sys.stdin.readline())
        num_list.append(num)
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    left = min_num
    right = max_num * M
    
    immigration(left,right)