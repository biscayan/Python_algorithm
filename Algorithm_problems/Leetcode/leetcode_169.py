from collections import defaultdict

# solution 1.
# runtime : 168ms, memory : 15.5mb
def majorityElement(nums):
    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1
    for k, v in counts.items():
        if v == max(counts.values()):
            return k

# solution 2.
# runtime : 264ms, memory : 15.6mb
def majorityElement(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    left = majorityElement(nums[:len(nums)//2])
    right = majorityElement(nums[len(nums)//2:])
    return [right,left][nums.count(left)>len(nums)//2]