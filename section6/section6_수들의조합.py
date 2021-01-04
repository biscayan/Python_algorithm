import sys

sys.stdin = open("input.txt", "r")

def DFS(lvl, start, num_sum):
    
    global count
    
    if lvl == K:
        
        if num_sum % M == 0:
            count += 1
        
    else:
        for i in range(start, N):
            DFS(lvl+1, i+1, num_sum+num_list[i])

if __name__ == '__main__':

    N, K = map(int,sys.stdin.readline().split())

    num_list = list(map(int,sys.stdin.readline().split()))

    M = int(sys.stdin.readline())

    count = 0

    DFS(0,0,0)

    print(count)