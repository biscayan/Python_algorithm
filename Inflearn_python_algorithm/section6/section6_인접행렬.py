import sys

sys.stdin = open("input.txt","r")

N, M = map(int, sys.stdin.readline().split())

matrix = [[0] * N for _ in range(N)]

for _ in range(M):
    
    ### x좌표, y좌표, 가중치
    x, y, w = map(int, sys.stdin.readline().split())
    
    matrix[x-1][y-1] = w

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=' ')
    print()