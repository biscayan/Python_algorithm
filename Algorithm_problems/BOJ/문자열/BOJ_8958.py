import sys

sys.stdin = open("input.txt", "r")

def calc_score(quiz):
    cnt, answer = 0, 0
    for q in quiz:
        if q == 'O':
            cnt += 1
            answer += cnt
        elif q == 'X':
            cnt = 0
    return answer

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        Q = sys.stdin.readline().strip()
        print(calc_score(Q))