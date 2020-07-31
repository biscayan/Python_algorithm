import sys
#sys.stdin=open("input.txt","rt")

T=int(input())

for i in range(T):
    N,s,e,k=map(int,input().split())
    num_list=list(map(int,input().split()))
    
    num_list2=num_list[s-1:e]
    num_list2.sort()
    print("#{0}".format(i+1),num_list2[k-1])


