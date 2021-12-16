def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    if stack:
        return 0
    else:
        return 1