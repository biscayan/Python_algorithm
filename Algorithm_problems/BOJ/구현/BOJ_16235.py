import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# spring
'''
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
'''
# summer
'''
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
'''
# autumn
'''
가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
'''
# winter
'''
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
'''

def tree_investment(land):
    year = 0
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    while year < K:
        # spring
        for i in range(N):
            for j in range(N):
                for k in range(len(land[i][j])):
                    if nutrients[i][j] >= land[i][j][k]:
                        nutrients[i][j] -= land[i][j][k]
                        land[i][j][k] += 1
                    else:
                        # summer
                        L = len(land[i][j])
                        for _ in range(L-k):
                            nutrients[i][j] += (land[i][j].pop()//2)
                        break
        # autumn
        for x in range(N):
            for y in range(N):
                for z in range(len(land[x][y])):
                    if land[x][y][z] % 5 == 0:
                        for i in range(8):
                            nx, ny = x+dx[i], y+dy[i]
                            if 0<=nx<N and 0<=ny<N:
                                land[nx][ny].appendleft(1)
        # winter
        for i in range(N):
            for j in range(N):
                nutrients[i][j] += A[i][j]

        year += 1

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += len(land[i][j])

    return answer

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    nutrients = [[5 for _ in range(N)] for _ in range(N)]
    
    trees = []
    land = [[deque() for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, sys.stdin.readline().split())
        trees.append((x,y,z))
    trees.sort(key = lambda x:x[2])
    for x,y,z in trees:
        land[x-1][y-1].append(z)

    print(tree_investment(land))