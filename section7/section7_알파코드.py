import sys

sys.stdin = open("input.txt", "r")

def alpha_code(lvl, pos):

    global count

    if lvl == n:
        for i in range(pos):
            
            ### 숫자를 알파벳으로 변환
            print(chr(numcode_list[i]+64), end='')
        
        count += 1
        
        print()

    else:
        for i in range(1,27):
            if i < 10:
                if num_list[lvl] == i:
                    numcode_list[pos] = i
                    alpha_code(lvl+1, pos+1)

            elif i >= 10:
                if i // 10 == num_list[lvl] and i % 10 == num_list[lvl+1]:
                     numcode_list[pos] = i
                     alpha_code(lvl+2, pos+1)

if __name__ =='__main__':

    num_list = list(map(int, sys.stdin.readline().strip()))

    n = len(num_list)

    ### out of index 방지
    num_list.insert(n,-1)

    numcode_list = [None] * n

    count = 0

    alpha_code(0,0)
    print(count)