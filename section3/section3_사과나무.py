import sys

sys.stdin=open('input.txt','r')

N=int(input())

farm= [list(map(int,input().split())) for _ in range(N)]

#print(farm)

pivot=N//2
l_idx,r_idx=pivot,pivot

apples=0

for i in range(N):
    for j in range(l_idx,r_idx+1,1):
        apples+=farm[i][j]

    #decrease left index, increase right index
    if i<pivot:
        l_idx-=1
        r_idx+=1

    #increase left index, decrease right index    
    elif i>=pivot:   
        l_idx+=1
        r_idx-=1

print(apples)


    
