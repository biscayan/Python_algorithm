def solution(x):
    x_list=list(str(x))
    int_x=0
    for i in range(len(x_list)):
        int_x+=int(x_list[i])
    if x%int_x==0:
        return True
    else:
        return False

if __name__=='__main__':
    #test case1
    arr=10
    print(solution(arr))

    #test case2
    arr=12
    print(solution(arr))

    #test case3
    arr=11
    print(solution(arr))

    #test case4
    arr=13
    print(solution(arr))
