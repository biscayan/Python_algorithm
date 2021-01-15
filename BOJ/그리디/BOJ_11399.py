import sys

# 1 + 1+2 + 1+2+3 + 1+2+3+3 + 1+2+3+3+4
# 1    3      6        9         13

sys.stdin = open("input.txt", "r")

def ATM(array):
    
    array.sort()

    result = 0
    current = 0

    for person in array:
        current += person
        result += current

    return result

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = list(map(int, sys.stdin.readline().split()))

    print(ATM(array))