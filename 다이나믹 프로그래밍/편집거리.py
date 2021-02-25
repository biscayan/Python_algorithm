import sys

sys.stdin = open("input.txt", "r")

def edit_distance(A, B):

    a_len, b_len = len(A), len(B)

    dp_table = [[0] * (b_len+1) for _ in range(a_len+1)]

    for i in range(a_len+1):
        dp_table[i][0] = i

    for j in range(b_len+1):
        dp_table[0][j] = j

    for i in range(1, a_len+1):
        for j in range(1, b_len+1):
            if A[i-1] == B[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
            else:
                ### 교체, 삽입, 삭제
                dp_table[i][j] = 1 + min(dp_table[i-1][j-1],dp_table[i][j-1],dp_table[i-1][j])

    result = dp_table[a_len][b_len]

    return result

if __name__ == '__main__':

    A, B = sys.stdin.readline().strip(), sys.stdin.readline().strip()

    print(edit_distance(A, B))