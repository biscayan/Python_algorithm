import sys

sys.stdin = open("input.txt","r")

def DFS(idx,sum):
    ###값의 절반을 넘으면 함수 중단, 시간복잡도 개선
    if sum>total//2:
        return

    if idx == N:
        if sum == (total-sum):
            ###YES를 출력하고 프로그램 종료
            print("YES")
            sys.exit(0)

    else:
        ###원소 사용
        DFS(idx+1,sum+elements[idx])
        ###원소 사용x
        DFS(idx+1,sum)


if __name__=='__main__':
    N = int(sys.stdin.readline())
    elements = list(map(int,sys.stdin.readline().split()))
                
    total = sum(elements)

    DFS(0,0)

    ###프로그램이 종료되지 않으면, 즉 YES를 출력하지 않으면 NO를 출력
    print("NO")