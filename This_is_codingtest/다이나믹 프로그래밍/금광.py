import sys

sys.stdin = open("input.txt", "r")

def gold_mine(n, m, array):

    dp_table = []
    idx = 0
    result = 0

    ### 2차원의 dp table 초기화
    for _ in range(n):
        dp_table.append(array[idx:idx+m])
        idx += m

    for j in range(1,m):
        for i in range(n):
            ### 이전 열의 왼쪽, 왼쪽아래에서 넘어옴
            if i == 0:
                dp_table[i][j] = dp_table[i][j] + max(dp_table[i][j-1], dp_table[i+1][j-1])
            ### 이전 열의 왼쪽, 왼쪽위에서 넘어옴
            elif i == n-1:
                dp_table[i][j] = dp_table[i][j] + max(dp_table[i][j-1], dp_table[i-1][j-1])
            ### 이전 열의 왼쪽, 왼쪽아래, 왼쪽위 모두에서 넘어옴
            else:
                dp_table[i][j] = dp_table[i][j] + max(dp_table[i][j-1], dp_table[i-1][j-1], dp_table[i+1][j-1])

    ### 마지막 열의 요소들을 비교
    for i in range(n):
        if dp_table[i][m-1] > result:
            result = dp_table[i][m-1]
    
    print(result)


if __name__ == '__main__':

    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split())
        array = list(map(int, sys.stdin.readline().split()))
        gold_mine(n, m, array)