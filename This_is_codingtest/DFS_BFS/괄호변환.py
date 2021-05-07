def divide_str(input_str):

    left_cnt, right_cnt = 0, 0

    for i in range(len(input_str)):
        if input_str[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            u = input_str[:i+1]
            v = input_str[i+1:]

            return u, v


def check_correct(input_str):

    stack = []

    for in_str in input_str:
        if in_str == '(':
            stack.append(in_str)
        elif in_str == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')

            else:
                stack.append(')')

    if stack:
        return False
    else:
        return True


def solution(p):

    ### step 1
    if p == '':
        return ''

    ### step 2
    u, v = divide_str(p)

    ### step 3
    if check_correct(u) == True:
        return u + solution(v)

    ### step 4
    else:
        answer = ''
        
        answer += '('
        answer += solution(v)
        answer += ')'
        
        for i in range(1, len(u)-1):
            if u[i] =='(':
                answer += ')'
            else:
                answer += '('

        return answer

if __name__ == '__main__':
    p = "()))((()"
    print(solution(p))