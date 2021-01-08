import sys
import time

sys.stdin = open("input.txt","r")

###풀이1
def Change1(n):
    
    if n == 1 or n == 3:
        return -1
    
    else:
        if n % 5 == 0:
            answer = n//5

        elif n % 5 == 1:
            answer = ((n//5)-1)+3

        elif n % 5 ==2:
            answer = (n//5)+1

        elif n % 5 ==3:
            answer = ((n//5)-1)+4

        elif n % 5 ==4:
            answer = (n//5)+2

    return answer

###풀이2
def Change2(n):

    count = 0

    if n==1 or n==3:
        return -1
    
    while n != 0:
        if n % 5 == 1 or n % 5 == 3:
            count += 1
            n -= 2

        elif n % 5 ==2 or n % 5 ==4:
            count += 1
            n -= 2

        elif n % 5 ==0:
            temp_count = n//5
            count += temp_count
            n %= 5

    return count

if __name__=='__main__':

    n = int(sys.stdin.readline())

    ###속도는 change2가 change1보다 빠름
    print(Change1(n))
    print(Change2(n))