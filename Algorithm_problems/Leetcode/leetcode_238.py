### solution1
### 시간초과
def productExceptSelf(nums):

    answer = []

    for i in range(len(nums)):

        mul = 1

        if i == 0:
            for j in range(1,len(nums)):
                mul *= nums[j]
            answer.append(mul)

        elif 0<i<len(nums)-1:
            for j in range(0,i):
                mul *= nums[j]
            for k in range(i+1,len(nums)):
                mul *= nums[k]
            answer.append(mul)

        elif i == len(nums)-1:
            for j in range(0,len(nums)-1):
                mul *= nums[j]
            answer.append(mul)

    return answer         


### solution2
### 232ms, 21MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        mul = 1

        for i in range(len(nums)):
            answer.append(mul)
            mul *= nums[i]

        mul = 1

        for j in range(len(nums)-1, -1, -1):
            answer[j] *= mul 
            mul *= nums[j]

        return answer