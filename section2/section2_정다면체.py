import sys
#sys.stdin=open("input.txt","rt")

N,M=map(int,input().split())

sum_list=[0]*(N+M)

n=0
N_list=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        sum_N_M=i+j-1
        sum_list[sum_N_M]+=1

num_max=0

for i in range(len(sum_list)):
    if sum_list[i]>num_max:
        num_max=sum_list[i]

for i in range(len(sum_list)):
    if num_max==sum_list[i]:
        print(i+1,end=' ')
    
