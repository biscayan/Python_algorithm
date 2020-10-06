###chr : ASCII -> Character
###ord : Character -> ASCII

'''
print(ord("a")) #97
print(ord("A")) #65
print(ord("z")) #122
print(ord("Z")) #90
'''

def solution(string, num):
    
    str_list = list(string)
    alnum = 26

    for i in range(len(str_list)):
        
        ###ignore space
        if str_list[i].islower():
            ###convert
            str_list[i] = chr((ord(str_list[i]) - ord("a") + num) % alnum + ord("a"))
            
        elif str_list[i].isupper():
            ###convert
            str_list[i] = chr((ord(str_list[i]) - ord("A") + num) % alnum + ord("A"))

    ###list -> str
    ###print로 하면 오류 발생
    return "".join(str_list)

if __name__=='__main__':
    ###test case1
    s = "AB"
    n = 1
    print(solution(s,n))

    ###test case2
    s = "z"
    n = 1
    print(solution(s,n))

    ###test case3
    s = "a B z"
    n = 4
    print(solution(s,n))
