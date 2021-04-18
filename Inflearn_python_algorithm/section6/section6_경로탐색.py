import sys

sys.stdin = open("input.txt", "r")

def DFS(v):

    global count

    ### 목적지에 도착하면 count + 1
    if v == N-1:
        count += 1

    else:
        for i in range(N):

            ### 갈 수 있는 경로가 존재하면서 방문하지 않았을 경우
            if matrix[v][i] == 1 and check[i] == False:
                check[i] = True
                DFS(i)
                check[i] = False

if __name__ == '__main__':

    N, M = map(int,sys.stdin.readline().split())

    matrix = [[0] * N for _ in range(N)]

    for _ in range(M):

        ### start, destination
        s_edge, d_edge = map(int,sys.stdin.readline().split())
        matrix[s_edge-1][d_edge-1] = 1

    check = [False] * N

    count = 0

    check[0] = True

    DFS(0)
    
    print(count)