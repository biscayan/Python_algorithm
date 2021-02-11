import sys

sys.stdin = open("input.txt", "r")

def Floyd_Warshall(array):

    ### 알고리즘
    for k in range(N):
        for i in range(N):
            for j in range(N):
                array[i][j] = min(array[i][j], array[i][k]+array[k][j])

    ### 정점이동 불가일때는 비용이 M
    for i in range(N):
        for j in range(N):
            if array[i][j] == 5000:
                array[i][j] = 'M'

    ### 결과 출력
    for i in range(N):
        for j in range(N):
            print(array[i][j], end=' ')
        print()


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    ### 테이블을 큰 값으로 초기화
    dp_table = [[5000] * N for _ in range(N)]

    ### 자기 자신의 노드는 0으로 초기화
    for i in range(N):
        dp_table[i][i] = 0

    ### 인접행렬
    for _ in range(M):
        i, j, cost = map(int, sys.stdin.readline().split())
        dp_table[i-1][j-1] = cost
    
    Floyd_Warshall(dp_table)