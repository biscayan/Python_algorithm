import sys

sys.stdin = open("input.txt","r")

def DFS(lvl):
    
    global count

    if lvl == M:
        for i in range(M):
            print(num_print[i], end=' ')

        print()
        
        count += 1

    else:
        for i in range(1,N+1):
            if num_check[i] == False:

                num_print[lvl] = i

                num_check[i] = True

                DFS(lvl+1)

                num_check[i] = False


if __name__ == '__main__':

    N, M = map(int,sys.stdin.readline().split())

    num_print = [0]*(N+1)

    num_check = [False]*(N+1)

    count = 0

    DFS(0)

    print(count)