import sys
sys.stdin = open("input.txt", "r")
N, k = map(int, sys.stdin.readline().split())
array = list(sys.stdin.readline().strip())
answer = 0
for i in range(N):
    if array[i] == 'P':
        left, right = i-k, i+k
        if left<0:
            left = 0
        if right > N-1:
            right = N-1
        for j in range(left, right+1):
            if array[j] == 'H':
                array[j] = 0
                answer += 1
                break
print(answer)