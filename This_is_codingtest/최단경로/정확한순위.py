import sys

sys.stdin = open("input.txt", "r")

def exact_rank(graph):

    result = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    if graph[i][k] == True and graph[k][j] == True:
                        graph[i][j] = True

    for i in range(N):
        count = 0
        for j in range(N):
            if graph[i][j] != False or graph[j][i] != False:
                count += 1
        if count == N-1:
            result += 1
            
    print(result)


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    graph = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        stud_a, stud_b = map(int, sys.stdin.readline().split())
        graph[stud_a-1][stud_b-1] = True

    exact_rank(graph)