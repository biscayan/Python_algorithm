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

    for _ in range(N):
        num = int(sys.stdin.readline())
        num_list.append(num)

    left = min(num_list)
    right = max(num_list) * M
    
    immigration(left,right)