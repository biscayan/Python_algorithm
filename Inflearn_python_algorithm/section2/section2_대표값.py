import sys
#sys.stdin=open("input.txt","rt")

N=int(input())
score_list=list(map(int,input().split()))

score_avg=round(sum(score_list)/N)

minx=2147000000 #매우 큰 값을 설정

for i,x in enumerate(score_list): #인데스와 값을 저장

    diff=abs(score_avg-x)

    if diff<minx:
        minx=diff
        score=x
        idx=i+1
        
    elif diff==minx: #>=일때는 맨 뒤의 번호를 return하게 됨
        if x>score:
            score=x
            idx=i+1
            
print(score_avg,idx)
        
