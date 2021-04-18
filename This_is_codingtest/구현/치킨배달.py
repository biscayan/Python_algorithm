import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")

def chicken_delivery(house_list, chicken_list):

    ### 아주 큰 값으로 초기화
    distance = 100000000

    for chickens in chicken_list:
        dist_sum = 0
        for house in house_list:
            tmp_dist = 100000000
            for chicken in chickens:
                tmp_dist = min(tmp_dist, abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))
            dist_sum += tmp_dist

        ### 거리의 최소값을 갱신
        distance = min(distance, dist_sum)

    return distance


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    house = []
    chicken = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i,j))

            if city[i][j] == 2:
                chicken.append((i,j))

    ### 폐업시키지 않을 치킨집을 조합으로 구함
    chicken_comb = list(combinations(chicken, M))

    print(chicken_delivery(house, chicken_comb))