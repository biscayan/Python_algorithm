import sys

sys.stdin = open("input.txt", "r")

def Ladder(x,y):

    visited[x][y] = True

    if x == 0:
        print(y)

    else:
        ### left
        if y-1 >= 0 and board[x][y-1] == 1 and visited[x][y-1] == False:
            Ladder(x,y-1)

        ### right
        elif y+1 < 10 and board[x][y+1] == 1 and visited[x][y+1] == False:
            Ladder(x,y+1)
            
        ### up
        else:
            ### 왼쪽, 오른쪽 모두 갈 수 없으면 위로 무조건 올라가야함
            Ladder(x-1,y)

if __name__ == '__main__':

    board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    visited = [[False] * 10 for _ in range(10)]

    ### 도착지점부터 역으로 출발지점을 탐색해서 올라감
    for i in range(10):
        if board[9][i] == 2:
            Ladder(9,i)