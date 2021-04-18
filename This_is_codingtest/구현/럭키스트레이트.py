import sys

sys.stdin = open("input.txt", "r")

def lucky_straight(num_list):

    ###숫자의 절반만 확인해도됨
    half_len = len(num_list)//2

    for i in range(half_len):
        if sum(num_list[:i+1]) == sum(num_list[i+1:]):
            print("LUCKY")
            break
    else:
        print("READY")


if __name__ == '__main__':
    N = list(map(int,sys.stdin.readline().strip()))

    lucky_straight(N)