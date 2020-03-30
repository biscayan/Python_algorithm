N,K=map(int,input().split())

array=[0]*(N+1)
cnt=0

for i in range(2,N+1):
    for j in range(i,N+1,i):
            if array[j]==0:
                array[j]=1
                cnt+=1
                if cnt==K:
                    print(j)
                    
                

            


                
