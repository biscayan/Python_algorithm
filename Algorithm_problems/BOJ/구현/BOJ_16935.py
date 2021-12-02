import sys
sys.stdin = open("input.txt", "r")

# 배열을 상하 반전시키는 연산
def rule1(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n): 
        new_array[i] = array[n-i-1]
    return new_array

# 배열을 좌우 반전시키는 연산
def rule2(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n): 
        for j in range(m): 
            new_array[i][j] = array[i][m-j-1]
    return new_array

# 오른쪽으로 90도 회전시키는 연산
def rule3(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_array[i][j] = array[n-j-1][i]
    return new_array

# 왼쪽으로 90도 회전시키는 연산
def rule4(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m): # 0 1 2 3 4 5 6 7
        for j in range(n): # 0 1 2 3 4 5
            new_array[i][j] = array[j][m-i-1]
    return new_array

# 5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다. 
# 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산
#    (1)      (2)
#  3 2 6 3  1 2 9 7
#  9 7 8 2  1 4 5 3
#  5 9 2 1  9 6 1 8
#    (4)      (3)
#  2 1 3 8  6 3 9 2
#  1 3 2 8  7 9 2 1
#  4 5 1 9  8 2 1 3

def rule5(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(m)] for _ in range(n)]
    # 1 -> 2
    for i in range(n//2): # 0 1 2
        for j in range(m//2,m): # 4 5 6 7
            new_array[i][j] = array[i][j-m//2]
    # 2 -> 3
    for i in range(n//2,n): # 3 4 5
        for j in range(m//2,m): # 4 5 6 7
            new_array[i][j] = array[i-n//2][j]
    # 3 -> 4
    for i in range(n//2,n): # 3 4 5
        for j in range(m//2): # 0 1 2 3
            new_array[i][j] = array[i][j+m//2]
    # 4 -> 1
    for i in range(n//2): # 0 1 2
        for j in range(m//2): # 0 1 2 3
            new_array[i][j] = array[i+n//2][j]
    return new_array

# 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산
#    (1)      (2)
#  3 2 6 3  1 2 9 7
#  9 7 8 2  1 4 5 3
#  5 9 2 1  9 6 1 8
#    (4)      (3)
#  2 1 3 8  6 3 9 2
#  1 3 2 8  7 9 2 1
#  4 5 1 9  8 2 1 3

def rule6(array):
    n, m = len(array), len(array[0])
    new_array = [[0 for _ in range(m)] for _ in range(n)]
    # 1 -> 4
    for i in range(n//2,n): 
        for j in range(m//2): 
            new_array[i][j] = array[i-n//2][j]
    # 4 -> 3
    for i in range(n//2,n): 
        for j in range(m//2,m):
            new_array[i][j] = array[i][j-m//2]
    # 3 -> 2
    for i in range(n//2): 
        for j in range(m//2,m): 
            new_array[i][j] = array[i-n//2][j]
    # 2 -> 1
    for i in range(n//2): 
        for j in range(m//2): 
            new_array[i][j] = array[i][j-m//2]
    return new_array

def calculation(array, calc_list):
    for calc in calc_list:
        if calc == 1:
            array = rule1(array)
        elif calc == 2:
            array = rule2(array)
        elif calc == 3:
            array = rule3(array)
        elif calc == 4:
            array = rule4(array)
        elif calc == 5:
            array = rule5(array)
        elif calc == 6:
            array = rule6(array)
    return array 

if __name__ == '__main__':
    N, M, R = map(int, sys.stdin.readline().split())
    array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    calc_list = list(map(int, sys.stdin.readline().split()))
    array = calculation(array, calc_list)
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print()