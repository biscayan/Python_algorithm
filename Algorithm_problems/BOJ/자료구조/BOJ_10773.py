import sys

sys.stdin = open("input.txt", "r")

def zero(k):

    stack = []

    for i in range(k):
        if num_list[i] != 0:
            stack.append(num_list[i])
        else:
            stack.pop()

    result = sum(stack)

    return result


if __name__ == '__main__':

    K = int(sys.stdin.readline())

    num_list = []

    for _ in range(K):

        num = int(sys.stdin.readline())
        num_list.append(num)

    print(zero(K))