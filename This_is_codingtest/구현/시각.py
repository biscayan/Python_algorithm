import sys

sys.stdin = open("input.txt","r")

def Time(N):

    count = 0

    ### hour
    for h in range(N+1):
        ### minute
        for m in range(60):
            ### second
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                    count += 1

    return count

if __name__ == '__main__':
    N  = int(sys.stdin.readline())

    print(Time(N))