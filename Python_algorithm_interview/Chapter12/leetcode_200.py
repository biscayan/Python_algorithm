from collections import deque

def numIslands(grid) -> int:

    def bfs(sx,sy):
        # up right down left
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]

        queue = deque([(sx,sy)])
        grid[sx][sy] = '0'

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx,ny))

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                bfs(i,j)
                count += 1
    
    return count