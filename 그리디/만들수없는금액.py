import sys

sys.stdin = open("input.txt","r")


def make_money(coins):

    coins.sort()

    answer = 0

    for coin in coins:

        if answer+1<coin:
            return answer+1

        else:
            answer+=coin

    return answer+1

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    num_list = list(map(int,sys.stdin.readline().split()))
    
    print(make_money(num_list))