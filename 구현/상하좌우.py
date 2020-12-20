import sys

sys.stdin = open("input.txt","r")

def LRUD(plans):
    
    x, y = 1, 1

    for plan in plans:

        if plan == "L":
            nx, ny = x, y-1

        elif plan == "R":
            nx, ny = x, y+1

        elif plan == "U":
            nx, ny = x-1, y

        elif plan == "D":
            nx, ny = x+1, y

        ###이동하려는 곳이 범위를 넘어가면 이동하지 않음
        if nx<1 or ny<1 or nx>5 or ny>5:
            continue
        
        ###좌표 갱신
        else:
            x, y = nx, ny

    print(x,y)


if __name__ == '__main__':
    N = int(sys.stdin.readline())

    move_plan = sys.stdin.readline().split()

    LRUD(move_plan)