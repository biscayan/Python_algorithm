import sys

sys.stdin=open('input.txt','r')

###Solve1
def str_check(string):
    
    string_list=list(string)

    while string_list:
        if string_list[0]==string_list[len(string_list)-1]:
            if len(string_list)!=1:
                string_list.pop(0)
                string_list.pop()
            else:
                string_list.pop(0)
        else:
            break
            
    if len(string_list)==0:
        return "YES"
    else:
        return "NO"


###Solve2
def str_check(string):
    reversed_string=''.join(reversed(string))
    #reversed_string=string[::-1]
    if string==reversed_string:
        return "YES"
    else:
        return "NO"


###Solve3
def str_check(string):
    for i in range(len(string)//2):
        if string[i]!=string[-1-i]:
            return "NO"
    else:
        return "YES"


if __name__=='__main__':
    N=int(input())

    for test_case in range(1,N+1):
        string=input()
        string=string.lower()
        check=str_check(string)
        print('#{} {}'.format(test_case,check))