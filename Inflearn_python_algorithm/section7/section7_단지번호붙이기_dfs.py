import sys

sys.stdin = open("input.txt", "r")

def house_grouping(x,y):

    global count

    count += 1

    house_map[x][y] = 0

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and house_map[nx][ny] == 1:
            house_grouping(nx,ny)


if __name__ == '__main__':
    
    N = int(sys.stdin.readline())

    house_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    count_list = []

    for row in range(N):
        for col in range(N):
            if house_map[row][col] == 1:
                count = 0
                house_grouping(row,col)
                count_list.append(count)

    count_list.sort()
    
    grouping_num = len(count_list)

    print(grouping_num)
    
    for houses in count_list:
        print(houses)