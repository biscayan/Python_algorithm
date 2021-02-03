import sys

sys.stdin = open("input.txt", "r")

def Muliplication(num1, num2):

    num3 = int(num1) * int(num2[2])
    num4 = int(num1) * int(num2[1])
    num5 = int(num1) * int(num2[0])

    num6 = num3 + 10*num4 + 100*num5
    
    print(num3)
    print(num4)
    print(num5)
    print(num6)
    
if __name__ == '__main__':

    num1, num2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()

    Muliplication(num1,num2)