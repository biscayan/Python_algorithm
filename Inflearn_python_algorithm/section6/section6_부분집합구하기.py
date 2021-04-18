import sys

sys.stdin = open("input.txt","r")

###상태트리
#1. 원소를 사용
#2. 원소를 사용x

def DFS(v):
    if v == N+1:
        for i in range(1, N+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    
    else:
        ###원소를 사용
        check[v] = 1
        DFS(v+1)

        ###원소를 사용x
        check[v] = 0
        DFS(v+1)

    

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    ###원소사용여부체크
    check = [0]*(N+1)

    DFS(1)