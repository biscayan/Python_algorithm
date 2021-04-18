import sys

sys.stdin = open("input.txt","r")

def DFS(lvl, start):

    global count

    if lvl == M:
        for i in range(M):
            print(num_seq[i], end=' ')

        count += 1

        print()
    
    else:
        for i in range(start,N+1):
            num_seq[lvl] = i
            DFS(lvl+1, i+1)


if __name__ == '__main__':
    
    N, M = map(int, sys.stdin.readline().split())

    count = 0

    num_seq = [0]*N
    
    DFS(0,1)

    print(count)