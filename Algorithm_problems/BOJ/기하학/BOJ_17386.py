import sys

sys.stdin = open("input.txt", "r")

###counterclockwise 판별함수
###값이 음수이면 counterclockwise, 양수이면 clockwise, 0이면 parallel
def ccw(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):

    part1 = p1_x * p2_y + p2_x * p3_y + p3_x * p1_y 
    part2 = p2_x * p1_y + p3_x * p2_y + p1_x * p3_y

    answer = part1 - part2

    return answer

if __name__ == "__main__":

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    
    ###값이 음수일 경우 counterclockwise
    if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) < 0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2) < 0:
        print(1)
    else:
        print(0)