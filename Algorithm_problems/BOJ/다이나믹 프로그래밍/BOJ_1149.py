import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    RGB = list(map(int, sys.stdin.readline().split()))
    array.append(RGB)

dp = [[] for _ in range(N)]
dp[0] = array[0]

for i in range(1,N):
    dp[i] = [array[i][0] + min(dp[i-1][1], dp[i-1][2]),
             array[i][1] + min(dp[i-1][0], dp[i-1][2]),
             array[i][2] + min(dp[i-1][0], dp[i-1][1])]
             
print(min(dp[N-1]))