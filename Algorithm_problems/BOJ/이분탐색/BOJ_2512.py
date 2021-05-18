import sys

sys.stdin = open("input.txt", "r")

def allocate_budget(budget_list):

    if sum(budget_list) <= M:
        return budget_list[-1]
    
    left, right = 1, budget_list[-1]
    max_budget = 0

    while left <= right:

        mid = (left+right) // 2
        budget_sum = 0

        for budget in budget_list:
            if budget > mid:
                budget_sum += mid
            else:
                budget_sum += budget

        if budget_sum > M:
            right = mid - 1
        else:
            left = mid + 1
            max_budget = mid
    
    return max_budget
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    budget_list = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    budget_list.sort()

    print(allocate_budget(budget_list))