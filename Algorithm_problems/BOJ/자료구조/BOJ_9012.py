import sys

def check_vps(string):
    stack = []
    for par in string:
        if par == '(':
            stack.append(par)
        elif par == ')':
            if stack: 
                if stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(par)
    if stack:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        check_vps(sys.stdin.readline().strip())