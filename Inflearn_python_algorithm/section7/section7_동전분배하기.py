import sys

sys.stdin = open("input.txt", "r")

def divide_coin(lvl):

    global result

    if lvl == N:
        if people_list[0] != people_list[1] and people_list[0] != people_list[2] and people_list[1] != people_list[2]:

            min_gap = max(people_list) - min(people_list)
            
            if min_gap < result:
                result = min_gap

    else:
        for i in range(3):
            people_list[i] += coin_list[lvl]
            divide_coin(lvl+1)
            people_list[i] -= coin_list[lvl]


if __name__ == '__main__':
    
    N = int(sys.stdin.readline())

    coin_list = []

    for _ in range(N):
        coin = int(sys.stdin.readline())
        coin_list.append(coin)

    people_list = [0] * 3

    result = 1000000

    divide_coin(0)

    print(result)