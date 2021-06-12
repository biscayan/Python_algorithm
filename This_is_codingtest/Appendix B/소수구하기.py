import sys
import math

def get_primenums(start, end):

    array = [True for _ in range(end+1)]
    array[1] = False

    for i in range(2, int(math.sqrt(end))+1):
        if array[i] == True:
            j = 2
            while i*j <= end:
                array[i*j] = False
                j += 1

    for num in range(start, end+1):
        if array[num] == True:
            print(num)

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    get_primenums(M,N)