import sys

sys.stdin = open("input.txt","r")

def up_to_down(array):
    
    sorted_array = sorted(array, reverse = True)

    for num in sorted_array:
        print(num, end =' ')

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    array = []

    for _ in range(N):
        num = int(sys.stdin.readline())
        array.append(num)

    up_to_down(array)