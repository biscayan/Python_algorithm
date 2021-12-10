from itertools import combinations

def solution(nums):
    answer = 0
    combs = list(combinations(nums,3))
    for comb in combs:
        flag = True
        num_sum = sum(comb)
        for i in range(2,num_sum):
            if num_sum % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer