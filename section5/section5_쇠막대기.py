import sys

sys.stdin = open("input.txt","r")

stick_list = list(sys.stdin.readline())

stack = []

stick_num = 0

for i in range(len(stick_list)):

    if stick_list[i] == '(':
        stack.append(stick_list[i])

    elif stick_list[i] == ')':
        ###레이저
        if stick_list[i-1] == '(':
            stack.pop()
            stick_num += len(stack)
        ###막대쌍
        else:
            stack.pop()
            stick_num += 1

print(stick_num)