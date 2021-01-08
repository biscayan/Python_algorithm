import sys

sys.stdin = open("input.txt", "r")


def antenna(houses):

    houses.sort()

    ### 안테나를 가장 중간에 있는 집에 설치하는 것이 최적의 선택임
    antenna = houses[(N-1) // 2]

    return antenna

if __name__ == '__main__':
    
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))

    print(antenna(num_list))