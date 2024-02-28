from itertools import combinations

def solution(number):
    answer = 0
    three_nums = list(combinations(number,3))
    for nums in three_nums:
        if sum(nums) == 0:
            answer += 1
    return answer