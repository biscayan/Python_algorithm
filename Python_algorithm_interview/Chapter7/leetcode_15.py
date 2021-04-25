### solution1
### Time Limit Exceeded
from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        combs = combinations(sorted(nums),3)

        for comb in combs:

            if sum(comb) == 0 and comb not in answer:
                answer.append(comb)

        return answer

### solution2
### 864ms, 17.6MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:

                num_sum = nums[i] + nums[left] + nums[right]

                if num_sum < 0:
                    left += 1

                elif num_sum > 0:
                    right -= 1

                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer