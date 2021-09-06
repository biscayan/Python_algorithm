import sys
from collections import deque
sys.stdin = open("input.txt", "r")

string = sys.stdin.readline().strip()
left, right = list(string), deque()
M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left+list(right)))