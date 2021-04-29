import sys

sys.stdin = open("input.txt", "r")

def tower(array):

    stack = []

    for i, num in enumerate(array):
        while True:
            if not stack:
                print(0, end=' ')
                stack.append((num,i))
                break
            
            else:
                if num > stack[-1][0]:
                    stack.pop()
                else:
                    ### 탑의 위치를 제대로 출력하기 위하여 +1
                    print(stack[-1][1]+1, end=' ')
                    stack.append((num,i))
                    break


if __name__ == '__main__':

    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))

    tower(num_list)