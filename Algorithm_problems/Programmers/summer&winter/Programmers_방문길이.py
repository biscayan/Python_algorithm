def solution(dirs):
    visited = []
    x, y = 5, 5
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    for dir in dirs:
        if dir == 'U':
            if 0<=x+dx[0]<11 and 0<=y+dy[0]<11:
                nx = x+dx[0]
                ny = y+dy[0]
                if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                    visited.append((x,y,nx,ny))
                x, y = nx, ny
        elif dir == 'R':
            if 0<=x+dx[1]<11 and 0<=y+dy[1]<11:
                nx = x+dx[1]
                ny = y+dy[1]
                if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                    visited.append((x,y,nx,ny))
                x, y = nx, ny
        elif dir == 'D':
            if 0<=x+dx[2]<11 and 0<=y+dy[2]<11:
                nx = x+dx[2]
                ny = y+dy[2]
                if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                    visited.append((x,y,nx,ny))
                x, y = nx, ny
        elif dir == 'L':
            if 0<=x+dx[3]<11 and 0<=y+dy[3]<11:
                nx = x+dx[3]
                ny = y+dy[3]
                if (x,y,nx,ny) not in visited and (nx,ny,x,y) not in visited:
                    visited.append((x,y,nx,ny))
                x, y = nx, ny
    return len(visited)