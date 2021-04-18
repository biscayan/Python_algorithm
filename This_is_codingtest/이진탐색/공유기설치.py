import sys

sys.stdin = open("input.txt","r")

def install_router(array):

    max_distance = 0

    ### 최소거리
    start = 1

    ### 최대거리
    end = array[-1] - array[0]

    while start <= end:
        
        ### 인접거리
        mid = (start + end) // 2

        router = array[0]
        count = 1

        for i in range(1,N):
            ### 공유기 설치 가능
            if array[i] >= router + mid:
                count += 1
                router = array[i]

        if count >= C:
            start = mid + 1
            max_distance = mid
        
        elif count < C:
            end = mid - 1
    
    return max_distance

if __name__ == '__main__':

    N, C = map(int, sys.stdin.readline().split())

    house_list = sorted([int(sys.stdin.readline()) for _ in range(N)])

    result = install_router(house_list)

    print(result)