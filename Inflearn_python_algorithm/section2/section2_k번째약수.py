import sys
#sys.stdin=open("input.txt","rt")

N, K=map(int,input().split())

k_list=[]

for i in range(1,N+1,1):
    if N%i==0:
        k_list.append(i)

if len(k_list)>=K:
    print(k_list[K-1])
else:
    print(-1)
