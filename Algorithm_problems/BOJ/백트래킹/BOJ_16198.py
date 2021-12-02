import sys
sys.stdin = open("input.txt", "r")

def dfs(array):
    if len(array) == 3:
        return array[0] * array[2]

    answer = 0
    for i in range(1, len(array)-1):
        result = array[i-1]*array[i+1] + dfs(array[:i]+array[i+1:])
        answer = max(answer, result)
        
    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    weights = list(map(int,sys.stdin.readline().split()))
    print(dfs(weights))