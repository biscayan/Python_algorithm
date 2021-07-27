def merge(intervals):
    stack = []
    intervals.sort()
    stack.append(intervals[0])
    answer = []
    for i in range(1, len(intervals)):
        if intervals[i][0] <= stack[-1][1]:
            if stack[-1][1] < intervals[i][1]:
                stack[-1][1] = intervals[i][1]
        else:
            answer.append(stack.pop())
            stack.append(intervals[i])
    answer += stack
    return answer