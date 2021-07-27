def largestNumber(nums):
    nums = list(map(str, nums))
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    if nums[0] == '0':
        return '0'

    answer = ''.join(nums)

    return answer