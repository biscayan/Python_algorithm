import sys

sys.stdin = open("input.txt", "r")

def Big_num(num_list):

    global M

    sorted_num_list = sorted(num_list, reverse = True)

    result = 0

    while True:

        ###K번만큼 연속으로 더함
        for _ in range(K):
            
            if M == 0:
                break

            result += sorted_num_list[0]
            M -= 1

        ###M번만큼 다 더했으면 종료
        if M == 0:
            break
        
        ###연속으로 더할 수 없을 때, 두번째로 큰 수를 더함
        result += sorted_num_list[1]
        M -= 1

    return result

if __name__ == '__main__':

    N, M, K = map(int,sys.stdin.readline().split())

    num_list = list(map(int,sys.stdin.readline().split()))

    print(Big_num(num_list))