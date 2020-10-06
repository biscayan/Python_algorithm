def solution(n):
    num_list=['1','2','4']
    num=''

    while n>0:
        #num은 1의자리->10의자리->100의 자리...순서로 저장
        
        #case for multiplication of 3 
        if n%3==0: 
            num=num_list[2]+num #1의 자리수의 값은 4
            n=(n//3)-1
            
        else:
            num=num_list[(n%3)-1]+num
            n=(n//3)
            
    return num
                    

if __name__=='__main__':
    #test case1
    n=1
    print(solution(n))
    
    #test case2
    n=2
    print(solution(n))

    #test case3
    n=3
    print(solution(n))

    #test case4
    n=4
    print(solution(n))

    #test case5
    n=5
    print(solution(n))

    #test case6
    n=6
    print(solution(n))

    #test case7
    n=7
    print(solution(n))

    #test case8
    n=8
    print(solution(n))

    #test case9
    n=9
    print(solution(n))

    #test case10
    n=10
    print(solution(n))

    #test case11
    n=11
    print(solution(n))

    #test case12
    n=12
    print(solution(n))

    #test case13
    n=13
    print(solution(n))
