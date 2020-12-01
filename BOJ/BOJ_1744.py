import sys

sys.stdin = open("input.txt","r")

def Bind_num(num_list):

    ###내림차순으로 정렬
    sorted_num_list = sorted(num_list,reverse=True)
    
    result = 0

    while sorted_num_list:
        if len(sorted_num_list) == 1:
            result += sorted_num_list.pop(0)

        else:
            ###1보다 클 때
            if sorted_num_list[0]>1:

                ###다음 값이 1보다 크면 묶음
                if sorted_num_list[1]>1:
                    result += (sorted_num_list.pop(0)*sorted_num_list.pop(0))

                ###다음값이 1이하이면 현재값만 더함
                elif sorted_num_list[1]<=1:
                    result += sorted_num_list.pop(0)

            ###1이면 현재값만 더함
            elif sorted_num_list[0]==1:
                result += sorted_num_list.pop(0)

            ###0일 때
            elif sorted_num_list[0]==0:

                ###남은 수가 홀수개면 현재값만 더함
                if len(sorted_num_list)%2==1:
                    result += sorted_num_list.pop(0)

                ###남은 수가 짝수개면 묶음
                else:
                    result += (sorted_num_list.pop(0)*sorted_num_list.pop(0))

            ###음수일 때
            elif sorted_num_list[0]<0:

                ###남은 수가 홀수개면 현재값만 더함
                if len(sorted_num_list)%2==1:
                    result += sorted_num_list.pop(0)

                ###남은 수가 짝수개면 묶음
                else:
                    result += (sorted_num_list.pop(0)*sorted_num_list.pop(0))

    print(result)

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    sequence = []

    for _ in range(N):
        num =int(sys.stdin.readline())
        sequence.append(num)
    
    Bind_num(sequence)