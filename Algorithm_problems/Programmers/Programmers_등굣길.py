def solution(m,n,puddles):

    route = [[0] * (m+1) for _ in range(n+1)]

    ###시작점
    route[1][1] = 1

    for i in range(1,n+1):
        for j in range(1, m+1):
            
            ###시작점은 pass
            if i==1 and j==1:
                continue
            
            ###웅덩이는 0
            if [j,i] in puddles:
                route[i][j] = 0
                
            ###이전의 경로를 더해나감
            else:
                route[i][j] += route[i-1][j] + route[i][j-1]
         
    answer = route[-1][-1] % 1000000007
    
    return answer

if __name__=='__main__':
    ###test case1
    m = 4
    n = 3
    puddles = [[2,2]]

    print(solution(m,n,puddles))
