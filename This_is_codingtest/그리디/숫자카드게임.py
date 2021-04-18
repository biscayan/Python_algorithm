import sys

sys.stdin = open("input.txt","r")

def Game(cards):

    card_max = 0

    for i in range(N):

        ###각 행에서 가장 작은 값을 저장
        temp_max = min(cards[i])

        if temp_max > card_max:
            card_max = temp_max

    return card_max

if __name__ =='__main__':

    N, M = map(int, sys.stdin.readline().split())

    card_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(Game(card_list))