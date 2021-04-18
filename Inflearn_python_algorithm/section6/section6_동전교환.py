import sys

sys.stdin = open("input.txt","r")

def change_coin(lvl, sum_num):

    global result

    if lvl>result:
        return

    if sum_num > M:
        return

    if sum_num == M:
        if lvl<result:
            result = lvl

    else:
        for i in range(N):
            change_coin(lvl+1,sum_num+sorted_coins[i])

if __name__ =='__main__':
    
    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    
    sorted_coins = sorted(coins,reverse=True)

    ###큰 숫자로 초기화
    result = 100000
    
    change_coin(0,0)

    print(result)