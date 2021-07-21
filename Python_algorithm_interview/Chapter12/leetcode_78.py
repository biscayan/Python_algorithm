from itertools import combinations

def subsets(nums):
    result = []
    for i in range(len(nums)+1):
        comb = list(combinations(nums, i))
        for x in comb:
            result.append(list(x))
    
    return result