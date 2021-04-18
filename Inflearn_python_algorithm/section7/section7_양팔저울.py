import sys

sys.stdin = open("input.txt","r")

def Scale(lvl, num):

    if lvl == K:
        
        ### 대칭구조가 만들어지므로 음수값은 추가하지 않아도 됨
        if 0<num<=S:
            water_list.add(num)
    
    else:
        ### 추를 왼쪽 저울에 추가
        Scale(lvl+1, num+num_list[lvl])

        ### 추를 오른쪽 저울에 추가
        Scale(lvl+1, num-num_list[lvl])

        ### 추를 추가하지 않음
        Scale(lvl+1, num)

if __name__ == '__main__':

    K = int(sys.stdin.readline())

    num_list = list(map(int,sys.stdin.readline().split()))

    S = sum(num_list)

    water_list = set()

    Scale(0, 0)

    result = S - len(water_list)

    print(result)