class Solution:
    def trap(self, height: List[int]) -> int:
        
        answer = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:

                last = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[last]

                answer += distance * waters

            stack.append(i)

        return answer