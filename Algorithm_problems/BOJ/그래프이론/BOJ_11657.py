import sys

sys.stdin = open("input.txt", "r")

def time_machine(graph):

    time[1] = 0

    for i in range(1, N+1):
        for start, end, bus in graph:
            if time[start] != INF and time[end] > time[start] + bus:
                if i == N:
                    return False
                time[end] = time[start] + bus
    return True

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    INF = 1e9
    graph = []
    time = [INF] * (N+1)

    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        graph.append((A,B,C))

    if not time_machine(graph):
        print(-1)
    else:
        for i in range(2,N+1):
            if time[i] != INF:
                print(time[i])
            else:
                print(-1)