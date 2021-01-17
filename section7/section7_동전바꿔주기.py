import sys

sys.stdin = open("input.txt", "r")

def change_coin(lvl, num_sum):

    global count

    if num_sum > T:
        return 

    if lvl == K:
        if num_sum == T:
            count += 1

    else:
        for i in range(coin_list[lvl][1]+1):
            change_coin(lvl+1, num_sum+(coin_list[lvl][0]*i))

if __name__ == '__main__':

    T = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    coin_list = []

    for _ in range(K):

        pi, ni = map(int, sys.stdin.readline().split())
        
        coin_list.append((pi,ni))

    count = 0

    change_coin(0,0)

    print(count)