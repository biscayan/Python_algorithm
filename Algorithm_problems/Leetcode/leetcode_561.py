class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()

        pair = []

        answer = 0

        for num in nums:

            pair.append(num)

            if len(pair) == 2:
                answer += pair[0]
                pair = []

        return answer