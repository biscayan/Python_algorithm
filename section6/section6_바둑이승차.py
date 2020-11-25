import sys

sys.stdin = open("input.txt","r")

def DFS(idx,sum, tsum):

    global result

    ###cut
    ###tsum:지금까지 판단을 한 무게
    if sum + (total-tsum) < result:
        return

    ###cut
    if sum>C:
        return

    if idx==N:
        if sum>result:
            result = sum
    else:
        DFS(idx+1, sum+dog_list[idx], tsum+dog_list[idx])
        DFS(idx+1, sum, tsum+dog_list[idx])


if __name__=='__main__':
    C,N = map(int,sys.stdin.readline().split())

    dog_list = []

    ###작은값으로 초기화
    result = -100000

    for i in range(N):
        dog_list.append(int(sys.stdin.readline()))
    
    total = sum(dog_list)

    DFS(0,0,0)

    print(result)