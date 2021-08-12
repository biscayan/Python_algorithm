def singleNumber(nums) -> int:
    answer = 0
    for num in nums:
        answer ^= num
    return answer