import sys

sys.stdin = open("input.txt", "r")

def vacation(lvl, pay):

    global result

    if lvl == N:
        if pay > result:
            result = pay

    else:
        if lvl+array[lvl][0] <= N:
            vacation(lvl+array[lvl][0], pay+array[lvl][1])
        vacation(lvl+1, pay)

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = []

    for _ in range(N):
        Ti, Pi = map(int, sys.stdin.readline().split())
        array.append((Ti,Pi))

    result = 0

    vacation(0, 0)

    print(result)