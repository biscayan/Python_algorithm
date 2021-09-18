from collections import deque
def maxSlidingWindow(nums, k):
    queue = deque()
    answer = []
    for i, v in enumerate(nums):
        while queue and nums[queue[-1]] < v:
            queue.pop()
        queue += i,
        if queue[0] == i - k:
            queue.popleft()
        if i >= k - 1:
            answer += nums[queue[0]]
    return answer