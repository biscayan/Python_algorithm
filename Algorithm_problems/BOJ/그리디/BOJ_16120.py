import sys

sys.stdin = open("input.txt", "r")

def PPAP_string(string):

    stack = []

    for s in string:

        stack.append(s)

        ### 스택의 마지막 4개의 문자가 PPAP이면 PPAP를 P로 바꿈
        if len(stack) >= 4:
            if stack[-4:] == ['P','P','A','P']:
                for _ in range(4):
                    stack.pop()
                stack.append('P')

    ### 최종 문자열
    result = ''.join(stack)

    if result == 'PPAP' or result == 'P':
        print('PPAP')
    else:
        print('NP')


if __name__ == '__main__':
    
    input_string = sys.stdin.readline().strip()

    PPAP_string(input_string)