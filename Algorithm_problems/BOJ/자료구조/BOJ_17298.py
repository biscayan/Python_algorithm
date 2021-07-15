import sys

sys.stdin = open("input.txt", "r")

def NGE(nums):

    stack = []
    result = [-1] * N

    for i in range(N):
        if stack:
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        else:
            stack.append(i)
                
    for i in range(len(result)):
        print(result[i], end=' ')

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    NGE(num_list)