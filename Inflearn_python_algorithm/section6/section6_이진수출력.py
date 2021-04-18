import sys

sys.stdin = open("input.txt","r")


def binary(n):

    if n == 0:
        return

    else:
        binary(n//2)
        print(n%2, end ='')


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    binary(N)