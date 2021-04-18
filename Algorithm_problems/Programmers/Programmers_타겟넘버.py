def DFS(numbers, target, idx, value):
    global answer

    if idx==len(numbers) and value == target:
        answer += 1
        return

    if idx==len(numbers):
        return

    DFS(numbers, target, idx+1, value+numbers[idx])
    DFS(numbers, target, idx+1, value-numbers[idx])
    

def solution(numbers, target):
    global answer

    DFS(numbers, target, 0, 0)

    return answer
    

if __name__=='__main__':

    answer = 0

    ###test case
    numbers = [1,1,1,1,1]
    target = 3

    print(solution(numbers,target))
