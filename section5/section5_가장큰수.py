import sys

sys.stdin = open("input.txt","r")

num, m = sys.stdin.readline().split()
m = int(m)
num_list = []

for n in num:
    num_list.append(int(n))

stack = []

for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m -= 1
    stack.append(x)

###모두 지우지 못한 경우
if m != 0:
    stack = stack[:-m]

print(''.join(map(str,stack)))