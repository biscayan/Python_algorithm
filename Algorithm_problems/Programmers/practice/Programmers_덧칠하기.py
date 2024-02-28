def solution(n, m, section):
    answer = 0
    point = section[0]-1
    for sec in section:
        if point < sec:
            point = sec+m-1
            answer += 1
    return answer