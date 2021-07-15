import sys

sys.stdin = open("input.txt", "r")

def mad_robot(x,y,p,cnt):

    global answer

    if cnt == N:
        answer += p
        return 

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        # not simple
        if board[nx][ny]:
            continue
        
        board[nx][ny] = 1
        mad_robot(nx,ny,p*possibility[i]*0.01,cnt+1)
        board[nx][ny] = 0

if __name__ == '__main__':
    inputs = list(map(int, sys.stdin.readline().split()))
    N, possibility = inputs[0], inputs[1:]

    answer = 0

    # east west south north
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    board = [[0] * (2*N+1) for _ in range(2*N+1)]
    board[N][N] = 1

    mad_robot(N,N,1,0)

    print(answer)