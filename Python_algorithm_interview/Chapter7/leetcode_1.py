### solution1
### 48ms, 14.5MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    
                    return answer


### solution2
### 48ms, 14.5MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {}
        
        for i, num in enumerate(nums):

            another_num = target-num

            if another_num in num_dict:
                answer = [num_dict[another_num], i]
                return answer

            else:
                num_dict[num] = i