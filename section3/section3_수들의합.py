import sys

sys.stdin=open("input.txt","r")

N,M=map(int,input().split())
num_list=list(map(int,input().split()))

count=0
i_idx=0
j_idx=1

#i index의 값으로 시작
num_sum=num_list[i_idx]

while True:
    if num_sum<M:
        if j_idx<N:
            num_sum+=num_list[j_idx]
            j_idx+=1
        #j index가 N에 도달
        else:
            break
    
    #m의 값이 되면 count +=1
    elif num_sum==M:
        num_sum-=num_list[i_idx]
        i_idx+=1
        count+=1

    elif num_sum>M:
        num_sum-=num_list[i_idx]
        i_idx+=1
        
print(count)
