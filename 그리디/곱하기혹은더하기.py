import sys

sys.stdin = open("input.txt","r")

def Calculation(num_list):
    
    answer = num_list[0]

    for i in range(1,len(num_list)):

        ###지금까지의 계산 결과가 0이거나 1이면 더함
        if answer == 0 or answer == 1:
            answer += num_list[i]

        else:
            
            ###현재 들어오는 값이 0이거나 1이면 더함
            if num_list[i] == 0 or num_list[i] == 1:
                answer += num_list[i]

            else:
                answer *= num_list[i]

    return answer
                

if __name__ == '__main__':
    num_list = list(map(int,sys.stdin.readline().strip()))
    print(Calculation(num_list))