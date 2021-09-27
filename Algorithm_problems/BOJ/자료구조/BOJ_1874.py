import sys
sys.stdin = open("input.txt", "r")

def check_stack(array):
    stack, result = [], []
    idx = 0
    for i in range(1, n+1):
        stack.append(i)
        result.append("+")
        while stack and stack[-1] == array[idx]:
            stack.pop()
            result.append("-")
            idx += 1
    if not stack:
        for op in result:
            print(op)
    else:
        print("NO")

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    sequence = []
    for _ in range(n):
        sequence.append(int(sys.stdin.readline()))
    check_stack(sequence)