import sys

sys.stdin = open("input.txt","r")

def move_knight(row, col):

    count = 0

    ###이동 최종 위치
    destination = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

    for des in destination:

        final_x = row + des[0]
        final_y = col + des[1]

        ###최종 위치가 정원 범위 안에 있으면 이동 가능
        if 1<=final_x<=8 and 1<=final_y<=8:
            count += 1

    return count


if __name__ == '__main__':

    location = sys.stdin.readline()

    row = int(location[1])
    col = int(ord(location[0])) - int(ord('a'))+1
    
    print(move_knight(row, col))