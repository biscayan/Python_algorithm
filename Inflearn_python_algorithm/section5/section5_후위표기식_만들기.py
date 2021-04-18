import sys

sys.stdin = open("input.txt", "r")

mid_calc = list(sys.stdin.readline())

oper_stack = []

seq = ''

for item in mid_calc:

    ###item이 숫자일때
    if item not in ['+','-','*','/','(',')']: #if item.isdecimal()
        seq += item

    else:
        if item == '(':
            oper_stack.append(item)

        elif item == '*' or item == '/':
            while oper_stack and (oper_stack[-1] =="*" or oper_stack[-1]=="/"):
                seq += oper_stack.pop()
            oper_stack.append(item)

        elif item == "+" or item == "-":
            while oper_stack and oper_stack[-1] != "(":
                seq += oper_stack.pop()
            oper_stack.append(item)

        elif item == ")":
            while oper_stack and oper_stack[-1] != "(":
                seq += oper_stack.pop()
            oper_stack.pop()

while oper_stack:
    seq += oper_stack.pop()

print(seq)