import sys
sys.stdin=open('input.txt','r')

def calc_score(n,score_list):

    result_list=[0]*n

    if score_list[0]==1:
        result_list[0]=1
    elif score_list[0]==0:
        result_list[0]=0

    for i in range(1,n): #1번 인덱스 ~ 마지막 인덱스
        if score_list[i]==0:
            result_list[i]=0
        elif score_list[i]==1 and score_list[i-1]==0:
            result_list[i]=1
        elif score_list[i]==1 and score_list[i-1]==1:
            result_list[i]=result_list[i-1]+1
        
    result_sum=sum(result_list)
    
    return result_sum


if __name__=='__main__':
    N=int(input())
    score_list=list(map(int,input().split()))
    print(calc_score(N,score_list))
