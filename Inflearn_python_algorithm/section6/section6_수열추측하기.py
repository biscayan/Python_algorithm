import sys

sys.stdin = open("input.txt","r")

def DFS(lvl,num_sum):
    if lvl == N and num_sum == F:
        for i in range(N):
            print(sequence[i], end =' ')
        
        ### 정답이 여러가지가 있다면 순서상 가장 앞에 정답으로 함
        sys.exit(0)

    else:
        for i in range(1,N+1):
            if num_check[i] == False:
                
                num_check[i] = True
                
                sequence[lvl] = i

                ### num_sum은 순열과 이항계수의 곱으로 표현가능함 
                DFS(lvl+1, num_sum + sequence[lvl]*binary[lvl])
                
                num_check[i] = False


if __name__ == '__main__':
    
    N, F = map(int, sys.stdin.readline().split())

    sequence = [0]*N

    binary = [1]*N

    num_check = [False] * (N+1)

    ### 이항계수 계산
    for i in range(1,N):
        binary[i] = binary[i-1]*(N-i)//i
    
    DFS(0,0)