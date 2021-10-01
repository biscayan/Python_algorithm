def fibonacci(n):
    global dp
    if n == 0:
        dp[0][0] = 1
    elif n == 1:
        dp[1][1] = 1
    else:
        for i in range(3):
            dp[n][i] = dp[n-1][i] + dp[n-2][i]

T = int(input())
for _ in range(T):
    N = int(input())
    # zero, one, value
    dp = [[0,0,0] for _ in range(N+1)]
    for i in range(N+1):
        fibonacci(i)
    print(dp[N][0], dp[N][1])