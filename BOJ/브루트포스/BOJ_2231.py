N=int(input())

position_sum=0

for i in range(1, N+1): 
    position_list=list(map(int,str(i)))
    position_sum=i+sum(position_list)

    if position_sum == N:
        print(i)
        break

    if i == N:
        print(0)

