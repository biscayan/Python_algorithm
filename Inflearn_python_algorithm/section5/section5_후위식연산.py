import sys

sys.stdin = open("input.txt", "r")

seq_list = list(sys.stdin.readline())

num_stack = []

for item in seq_list:
    if item.isdecimal():
        num_stack.append(item)

    elif item == '+':
        num_sum = int(num_stack[-2]) + int(num_stack[-1])
        num_stack.pop()
        num_stack.pop()
        num_stack.append(num_sum)

    elif item == '-':
        num_minus = int(num_stack[-2]) - int(num_stack[-1])
        num_stack.pop()
        num_stack.pop()
        num_stack.append(num_minus)

    elif item == '*':
        num_mul = int(num_stack[-2]) * int(num_stack[-1])
        num_stack.pop()
        num_stack.pop()
        num_stack.append(num_mul)

    elif item == '/':
        num_div = int(num_stack[-2]) / int(num_stack[-1])
        num_stack.pop()
        num_stack.pop()
        num_stack.append(num_div)


print(num_stack[0])
