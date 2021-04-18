import sys

sys.stdin = open("input.txt", "r")

def resignation(n):

    dp_table = [0] * (n+1)

    max_value = 0

    ### array를 거꾸로 체크
    for i in range(n-1,-1,-1):

        ti, pi = array[i]

        ### 퇴사 하기 전의 기간 안에 있다면
        if ti+i <= n:
            dp_table[i] = max(dp_table[ti+i]+pi, max_value)
            max_value = dp_table[i]

        ### 범위를 벗어난다면
        else:
            dp_table[i] = max_value
    
    return max_value
            

if __name__ == '__main__':
    
    N = int(sys.stdin.readline())

    array = []

    for _ in range(N):
        Ti, Pi = map(int, sys.stdin.readline().split())
        array.append((Ti, Pi))

    print(resignation(N))