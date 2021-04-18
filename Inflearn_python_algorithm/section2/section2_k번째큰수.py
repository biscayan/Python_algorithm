import sys
#sys.stdin=open("input.txt","rt")

N,K=map(int,input().split())

num_list=list(map(int,input().split()))
res_set=set()
for i in range(N):
    for j in range(i+1,N):
        for l in range(j+1,N):
            res_set.add(num_list[i]+num_list[j]+num_list[l])
            
res_list=list(res_set)
res_list.sort(reverse=True)

print(res_list[K-1])
