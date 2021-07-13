from itertools import product

def letterCombinations(digits: str):

    answer = []

    if digits == '':
        return answer

    mapping = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
                '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                '8':['t','u','v'], '9':['w','x','y','z']}

    alpbabet_list = []

    for digit in digits:
        alpbabet_list.append(mapping[digit])

    comb_list = list(product(*alpbabet_list))

    for i in range(len(comb_list)):
        answer.append(''.join(comb_list[i]))

    return answer