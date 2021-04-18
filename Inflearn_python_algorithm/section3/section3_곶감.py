import sys

sys.stdin = open("input.txt","r")

N = int(input())
lattice = [list(map(int,input().split())) for _ in range(N)]
M = int(input())

for _ in range(M):

    row, direction, rotation = map(int,input().split())

    #right rotation
    if direction==0:
        for _ in range(rotation):
            lattice[row-1].append(lattice[row-1].pop(0))

    #left rotation
    elif direction==1:
        for _ in range(rotation):
            lattice[row-1].insert(0,lattice[row-1].pop())


l_idx = 0
r_idx = N
res = 0

for i in range(N):
    for j in range(l_idx, r_idx, 1):
        res+=lattice[i][j]

    if i<N//2:
        l_idx+=1
        r_idx-=1
        
    elif i>=N//2:
        l_idx-=1
        r_idx+=1
        
print(res)
        
        
