def solution(numbers):
    
    answer=''
    numbers=list(map(str,numbers))
    
    ###bubble sort
    for i in range(len(numbers)-1):
        for j in range(0,len(numbers)-1,1):

            ###맨 앞자리 비교

            ###값이 작으면 swap
            if numbers[j][0]<numbers[j+1][0]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

            ###값이 같으면, 그 다음을 비교
            elif numbers[j][0]==numbers[j+1][0]:
                
                int1=int(numbers[j]+numbers[j+1])
                int2=int(numbers[j+1]+numbers[j])
                        
                if int1<int2:
                    numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

    for num in numbers:
        answer+=num

    return answer

if __name__=='__main__':
    
    #test_case1
    numbers=[6,10,2]
    print(solution(numbers))
    
    #test_case2
    numbers=[3,30,34,5,9]
    print(solution(numbers))
    

#####문제점1. 절반은 시간초과 -> bubble sort가 속도가 느리기 떄문..?
#####문제점2. 100의 자리 수는 어떻게 처리??
