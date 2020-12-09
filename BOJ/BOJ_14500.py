import sys

sys.stdin = open("input.txt","r")

###BOJ 테스트 통과 실패, 무엇이 문제일까..

def Tetromino(x,y):

    global result

    ###나올 수 있는 모양의 경우의 수 -> 19
    for i in range(len(tetro)):
        
        num_sum = paper[x][y]

        for j in range(3):

            nx = x + tetro[i][j][0]
            ny = y + tetro[i][j][1]
                
            ###범위 내에 있는 값일 경우에 수를 더함
            if 0<=nx<=N-1 and 0<=ny<=M-1:
                num_sum += paper[nx][ny]
        
        ###수들의 합이 현재보다 더 클 경우 값을 바꿈
        if num_sum > result:
            result = num_sum


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = 0

    tetro = [
            ###shape1 (ㅡ)
            [(0,1),(0,2),(0,3)],
            [(1,0),(2,0),(3,0)],

            ###shape2 (ㅁ)
            [(0,1),(1,0),(1,1)],

            ###shape3 (L)
            [(1,0),(2,0),(2,1)],
            [(1,0),(0,1),(0,2)],
            [(0,1),(1,1),(2,1)],
            [(0,1),(0,2),(-1,2)],
            ###reversed shape3
            [(1,0),(2,0),(2,-1)],
            [(1,0),(1,1),(1,2)],
            [(0,1),(1,0),(2,0)],
            [(0,1),(0,2),(1,2)],

            ###shape4 (ㄴㄱ)
            [(1,0),(1,1),(2,1)],
            [(0,1),(-1,1),(-1,2)],
            ###reversed shape4
            [(1,0),(1,-1),(2,-1)],
            [(0,1),(1,1),(1,2)],

            ###shape5 (ㅜ)
            [(0,1),(0,2),(1,1)],
            [(0,1),(-1,1),(2,1)],
            [(0,1),(-1,1),(0,2)],
            [(1,0),(2,0),(1,1)]
            ]

    for i in range(N):
        for j in range(M):
            Tetromino(i,j)

    print(result)