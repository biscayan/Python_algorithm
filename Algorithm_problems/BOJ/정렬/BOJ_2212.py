import sys

sys.stdin = open("input.txt", "r")

def sensor(array):
    
    array.sort()

    distance_list = []

    ### 집중국이 센서보다 많이 있으면 센서마다 집중국을 설치할 수 있으므로 최소 길이는 0
    if N <= K:
        min_distance = 0
        return min_distance

    ### 센서들 사이의 거리를 계산해서 리스트에 넣어줌
    for i in range(1, N):
        sensor_distance = array[i] - array[i-1]
        distance_list.append(sensor_distance)

    distance_list.sort()

    ### 거리가 큰 경우들을 k-1번 만큼 제거
    for _ in range(K-1):
        distance_list.pop()

    min_distance = sum(distance_list)

    return min_distance

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    array = list(map(int,sys.stdin.readline().split()))

    print(sensor(array))