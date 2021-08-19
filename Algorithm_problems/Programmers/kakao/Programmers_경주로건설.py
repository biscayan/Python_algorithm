from collections import deque

def bfs(sx,sy,sc,sd,board):
    N = len(board)
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    queue = deque([(sx,sy,sc,sd)])
    cost = [[1e9] * N for _ in range(N)]
    cost[0][0] = 0

    while queue:
        x, y, c, d = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1:
                if i == d:
                    nc = c + 100
                else:
                    nc = c + 600
                if nc < cost[nx][ny]:
                    cost[nx][ny] = nc
                    queue.append((nx,ny,nc,i))
    
    return cost[-1][-1]

def solution(board):
    answer = min(bfs(0,0,0,1,board), bfs(0,0,0,2,board))
    return answer