import sys

sys.stdin = open("input.txt", "r")

def Build_tower(n):

    result = 0

    dp_table = [0] * n

    dp_table[0] = bricks[0][1]

    for i in range(1,n):
        max_h = 0
        for j in range(i):
            if bricks[i][2] < bricks[j][2] and dp_table[j] > max_h:
                max_h = dp_table[j]

        dp_table[i] = max_h + bricks[i][1]

        result = max(result, dp_table[i])

    print(result)


if __name__ == '__main__':

    n = int(sys.stdin.readline())

    bricks = []

    for _ in range(n):
        area, height, weight = map(int, sys.stdin.readline().split())
        bricks.append((area,height,weight))
    
    ### area를 기준으로 정렬
    bricks.sort(key = lambda x:-x[0])

    Build_tower(n)