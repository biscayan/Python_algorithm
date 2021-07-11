from itertools import permutations

def permute(nums):
    answer = list(permutations(nums, len(nums)))
    return answer