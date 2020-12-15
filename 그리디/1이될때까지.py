import sys

sys.stdin = open("input.txt","r")

def Calculation(N, K):

    count = 0

    while N > 1:

        if N % K == 0:
            N /= K
            count += 1

        else:
            N -= 1
            count += 1

    ### N이 1이 되면 종료
    return count


if __name__ == '__main__':

    N, K = map(int, sys.stdin.readline().split())

    print(Calculation(N, K))