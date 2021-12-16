def solution(d, budget):
    answer = 0
    sorted_d = sorted(d)
    for num in sorted_d:
        if budget >= num:
            budget -= num
            answer += 1
        else:
            break
    return answer