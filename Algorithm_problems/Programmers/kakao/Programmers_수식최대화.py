import copy
from collections import deque
from itertools import permutations

def preprocessing(expression, operators):

    for i in range(len(operators)):
        expression = expression.replace(f'{operators[i]}', f' {operators[i]} ')

    expression_list = expression.split(' ')
    
    return expression_list


def plus(expression_list, operator):

    calc_result = []
    expression_list = deque(expression_list)

    while expression_list:
        if expression_list[0] == operator:
            expression_list.popleft()
            value = int(calc_result.pop()) + int(expression_list.popleft())
            calc_result.append(value)
        else:
            calc_result.append(expression_list.popleft())

    return calc_result


def minus(expression_list, operator):

    calc_result = []
    expression_list = deque(expression_list)

    while expression_list:
        if expression_list[0] == operator:
            expression_list.popleft()
            value = int(calc_result.pop()) - int(expression_list.popleft())
            calc_result.append(value)
        else:
            calc_result.append(expression_list.popleft())

    return calc_result


def mul(expression_list, operator):

    calc_result = []
    expression_list = deque(expression_list)

    while expression_list:
        if expression_list[0] == operator:
            expression_list.popleft()
            value = int(calc_result.pop()) * int(expression_list.popleft())
            calc_result.append(value)
        else:
            calc_result.append(expression_list.popleft())

    return calc_result


def solution(expression):

    answer = 0

    operators = set()

    for exp in expression:
        if not exp.isdigit():
            operators.add(exp)

    ### 사용된 연산자를 확인
    operators = list(operators)

    ### 모든 연산자 사용순서 
    priorities = list(permutations(operators, len(operators)))

    ### expression 전처리
    expression_list = preprocessing(expression, operators)
    
    for priority in priorities:

        calc_list = copy.deepcopy(expression_list)

        for operator in priority:
            if operator =='+':
                calc_list = plus(calc_list, operator)
            elif operator =='-':
                calc_list = minus(calc_list, operator)
            elif operator =='*':
                calc_list = mul(calc_list, operator)

        answer = max(answer, abs(sum(calc_list)))

    return answer


if __name__ == '__main__':

    expression = "100-200*300-500+20"
    print(solution(expression))