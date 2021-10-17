import sys
sys.stdin = open("input.txt", "r")

def check(left, right, sign):
    if sign == '<':
        if int(left) > right:
            return False
    elif sign == '>':
        if int(left) < right:
            return False
    return True

def backtracking(lvl, num_str):
    global candidate

    if lvl == k+1:
        candidate.append(num_str)
        return
    
    for i in range(10):
        if not visited[i]:
            if lvl == 0 or check(num_str[-1], i, sign_array[lvl-1]):
                visited[i] = True
                backtracking(lvl+1, num_str+str(i))
                visited[i] = False

if __name__ == '__main__':
    k = int(sys.stdin.readline())
    sign_array = list(sys.stdin.readline().split())
    candidate = []
    visited = [False] * 10
    backtracking(0, "")
    print(candidate[-1])
    print(candidate[0])