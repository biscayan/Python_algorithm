import sys

sys.stdin = open("input.txt", "r")

def pizza_delivery(lvl,start):

    global result

    if lvl == M:

        distance_sum = 0

        for i in range(len(house_list)):

            house_x, house_y = house_list[i][0], house_list[i][1]

            distance = 10000000

            for idx in combination:

                pizza_x, pizza_y = pizza_list[idx][0], pizza_list[idx][1]

                ### 집과 피자집 사이의 거리를 계산
                tmp_distance = abs(house_x - pizza_x) + abs(house_y - pizza_y)

                ### 하나의 집과 여려개의 피자집들 중에서 가장 작은 거리를 저장
                distance = min(distance, tmp_distance)

            ### 다음집의 거리를 구하기 위해 현재집의 거리를 sum에 저장
            distance_sum += distance

        if distance_sum < result:
            result = distance_sum

    else:
        ### 피자집의 조합구하기, 인덱스를 저장 
        for i in range(start, len(pizza_list)):
            combination[lvl] = i
            pizza_delivery(lvl+1, i+1)

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    ### 0 -> 빈칸 / 1 -> 집 / 2 -> 피자집
    city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    house_list, pizza_list = [], []

    ### M개의 피자집의 조합의 수
    combination = [0] * M

    result = 10000000

    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:
                house_list.append((i,j))
            elif city_map[i][j] == 2:
                pizza_list.append((i,j))

    pizza_delivery(0,0)

    print(result)