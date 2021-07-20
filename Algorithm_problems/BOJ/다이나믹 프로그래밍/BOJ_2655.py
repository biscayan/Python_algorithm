import sys

sys.stdin = open("input.txt", "r")

# LIS algorithm
def build_tower(bricks):

    result = []

    # sort the array based on the weight
    bricks.sort(key = lambda x:x[3])
    # print(bricks)

    # store the height
    dp_table = [0] * (n+1)

    for i in range(1,n+1):
        for j in range(i):
            if bricks[i][1] > bricks[j][1]:
                dp_table[i] = max(dp_table[i], dp_table[j]+bricks[i][2])
    
    # print(dp_table)
    max_height = max(dp_table)
    idx = dp_table.index(max_height)

    while max_height != 0:
        if max_height == dp_table[idx]:
            result.append(bricks[idx][0])
            max_height -= bricks[idx][2]
        idx -= 1

    result.reverse()

    print(len(result))
    for x in result:
        print(x)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    brick_list = []
    brick_list.append((0,0,0,0))
    for i in range(1, n+1):
        width, height, weight = map(int, sys.stdin.readline().split())
        brick_list.append((i, width, height, weight))

build_tower(brick_list)