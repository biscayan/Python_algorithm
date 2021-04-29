import sys
import re
from collections import deque

sys.stdin = open("input.txt", "r")

def AC(num_list, rule_list):

    num_deque = deque(num_list)

    ### 에러발생 여부 체크
    error = False

    ### reverse여부 체크, reverse() 메소드를 사용하면 시간초과 발생
    sign = 1

    for rule in rule_list:
        if rule == "R":
            sign *= -1

        elif rule == "D":
            if not num_deque:
                error = True
                break
            else:
                if sign == 1:
                    num_deque.popleft()
                else:
                    num_deque.pop()

    if not error:
        if sign == 1:
            print('[', end='')
            print(','.join(num_deque),end='')
            print(']')

        else:
            print('[', end='')
            print(','.join(reversed(num_deque)),end='')
            print(']')

    else:
        print("error")


if __name__ == '__main__':

    T = int(sys.stdin.readline())

    for _ in range(T):

        p = list(sys.stdin.readline().strip())
        n = int(sys.stdin.readline())

        input_numstr = re.sub("[^0-9]", " ", sys.stdin.readline().strip())

        ### 주의! 숫자들을 int로 변경하면 안됨
        array = list(input_numstr.split())
        
        AC(array, p)