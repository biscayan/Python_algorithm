def solution(n):
    num_list=['1','2','4']
    num=''
    #num은 1의자리->10의자리->100의 자리...순서로 저장
    while n>0:  
        #case for multiplication of 3 
        if n%3==0: 
            num=num_list[2]+num #1의 자리수의 값은 4
            n=(n//3)-1
        else:
            num=num_list[(n%3)-1]+num
            n=(n//3)
    return num