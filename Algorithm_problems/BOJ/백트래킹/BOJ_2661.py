def backtracking(ans):
    for i in range(1,len(ans)//2+1):
        left = ans[len(ans)-2*i:len(ans)-i]
        right = ans[len(ans)-i:]
        if left == right:
            return

    if len(ans) == N:
        print(int(ans))
        exit()

    for num in ["1", "2", "3"]:
        backtracking(ans+num)

N = int(input())
backtracking("1")