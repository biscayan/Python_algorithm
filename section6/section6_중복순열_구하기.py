import sys

sys.stdin = open("input.txt","r")

def DFS(L):
    global count

    if L == M:
        for i in range(M):
            print(nums[i], end=' ')

        count += 1

        print()

    else:
        for i in range(1,N+1):
            nums[L] = i
            DFS(L+1)


if __name__=='__main__':
    N, M = map(int,input().split())
    
    count = 0

    nums = [0]*N

    DFS(0)
    
    print(count)