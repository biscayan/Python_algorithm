import sys

sys.stdin = open("input.txt", "r")

L = int(sys.stdin.readline())

box_list = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())

for _ in range(M):
    box_list[0] += 1
    box_list[-1] -= 1
    box_list.sort()

print(box_list[-1] - box_list[0])
