import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

left_index = 0
right_index = N-1

seq_len = 0
seq_str = ''

###수열의 마지막 숫자를 저장
seq_last = 0

stack = []

while left_index <= right_index:

    if num_list[left_index] > seq_last:
        stack.append((num_list[left_index],"L"))
        
    if num_list[right_index] > seq_last:
        stack.append((num_list[right_index],"R"))

    stack.sort()

    if len(stack) == 0:
        break
    else:
        seq_str += stack[0][1]
        seq_last = stack[0][0]
        seq_len += 1

        if stack[0][1] == "L":
            left_index += 1
            
        elif stack[0][1] == "R":
            right_index -= 1

    stack.clear()

print(seq_len)
print(seq_str)