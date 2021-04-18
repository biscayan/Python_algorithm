import sys

sys.stdin = open("input.txt", "r")

def Alibaba(x,y):

    ### cut edge
    if memoization[x][y] != 0:
        return memoization[x][y]

    ### end point
    if x == 0 and y == 0:
        return board[0][0]

    ### memoization
    else:
        if x == 0 and y != 0:
            memoization[x][y] = Alibaba(x, y-1) + board[x][y]

        elif x != 0 and y == 0:
            memoization[x][y] = Alibaba(x-1, y) + board[x][y]

        elif x != 0 and y != 0:
            memoization[x][y] = min(Alibaba(x-1, y), Alibaba(x, y-1)) + board[x][y]

        return memoization[x][y]


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    memoization = [[0] * N for _ in range(N)]

    print(Alibaba(N-1, N-1))