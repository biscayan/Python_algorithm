import sys

sys.stdin = open("input.txt", "r")

def matrix(A,B):

    answer = 0

    ### N/M-3+1
    for i in range(N-2):
        for j in range(M-2):
            
            ### 행렬 A와 B가 다르다면 원소들을 모두 뒤집기
            if A[i][j] != B[i][j]:
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        A[k][l] = 1 - A[k][l]

                answer += 1

    if A == B:
        return answer
    else:
        return -1


if __name__ == '__main__':

    N, M = map(int,sys.stdin.readline().split())

    A = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
    B = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

    print(matrix(A,B))