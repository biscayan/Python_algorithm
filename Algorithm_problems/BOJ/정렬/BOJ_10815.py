import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
num_set = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
for num in num_list:
    if num in num_set:
        print(1, end=' ')
    else:
        print(0, end=' ')