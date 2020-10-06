def solution(brown,yellow):
    
    for height in range(1, yellow+1):
        
        #가로 >= 세로
        #가로 -> width, 세로 -> i   
        if yellow % height == 0:
            width = yellow//height

            #total-yellow==brown
            #테두리는 2를 추가
            if (width + 2)*(height + 2) - (width * height) == brown:
                return [width+2, height+2]
                

if __name__=='__main__':
    #test case1
    brown=10
    yellow=2
    print(solution(brown,yellow)) #[4,3]

    #test case2
    brown=8
    yellow=1
    print(solution(brown,yellow)) #[3,3]

    #test case3
    brown=24
    yellow=24
    print(solution(brown,yellow)) #[8,6]

    #test case4
    brown=12
    yellow=3
    print(solution(brown,yellow)) #[5,3]

    #test case5
    brown=18
    yellow=12
    print(solution(brown,yellow)) #[6,5]
