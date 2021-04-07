import sys

sys.stdin = open("input.txt", "r")

def gas_station(road, city):

    idx = 0
    answer = road[idx] * city[idx]

    for i in range(1, N-1):
        
        ### 다음 도시의 숫자가 더 작으면 인덱스를 바꿈
        if city[i] < city[idx]:
            idx = i
        
        answer += road[i] * city[idx]

    return answer


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    road_list = list(map(int, sys.stdin.readline().split()))
    city_list = list(map(int, sys.stdin.readline().split()))

    ### 마지막 도시 정보는 필요가 없음
    print(gas_station(road_list, city_list[:-1]))