import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

def find_mode(array):

    counter = Counter(array)

    ### (값, 빈도)의 튜플로 묶음
    modes = counter.most_common()
    frequency = modes[0][1]

    if len(modes) == 1:
        mode = modes[0][0]
    else:
        ### 최빈값이 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 리턴
        if modes[1][1] == frequency:
            mode = modes[1][0]
        ### 그렇지 않다면 가장 작은 값을 리턴
        else:
            mode = modes[0][0]
    
    return mode


def statistics(array):

    ### 산술평균
    mean = int(round(sum(array) / len(array), 0))

    ### 중앙값
    median = array[len(array)//2]
    
    ### 최빈값
    mode = find_mode(array)

    ### 범위
    min_max = array[-1] - array[0]

    print(mean)
    print(median)
    print(mode)
    print(min_max)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    num_list = []

    for _ in range(N):
        num = int(sys.stdin.readline())
        num_list.append(num)

    num_list.sort()

    statistics(num_list)