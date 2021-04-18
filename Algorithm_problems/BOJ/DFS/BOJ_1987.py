import sys
import string
from collections import deque

sys.stdin = open("input.txt","r")

def DFS(x,y,cnt):

    global answer

    answer = max(answer, cnt)

    for i in range(4):

        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<R and 0<=ny<C and not check[ord(board[nx][ny])-65]:
            check[ord(board[nx][ny])-65] = True
            DFS(nx,ny,cnt+1)
            check[ord(board[nx][ny])-65] = False


if __name__ == '__main__':

    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    ### from A to Z
    check = [False] * 26
    check[ord(board[0][0])-65] = True
    answer = 1

    DFS(0,0,1)

    print(answer)