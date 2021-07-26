### zero padding이 된 확장된 자물쇠 만들기
def make_extended_lock(lock):

    n = len(lock)

    extended_lock = [[0] * (3*n) for _ in range(3*n)]

    for i in range(n):
        for j in range(n):
            extended_lock[i+n][j+n] = lock[i][j]

    return extended_lock

### 오른쪽 90도 방향으로 key를 회전
def rotation(key):
    
    m = len(key)

    rotated_key = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rotated_key[j][m-i-1] = key[i][j]

    return rotated_key

### 원래의 lock부분을 확인
def check(new_lock):

    start = len(new_lock) // 3
    end = start * 2

    for i in range(start, end):
        for j in range(start, end):
            ### 값이 1이 아니면 제대로 껴진 것이 아님
            if new_lock[i][j] != 1:
                return False

    return True


def solution(key, lock):

    n, m = len(lock), len(key)

    extended_lock = make_extended_lock(lock)

    ### 네 방향 회전을 하면서 key가 lock에 맞는지를 확인, 완전탐색
    for _ in range(4):

        key = rotation(key)

        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        extended_lock[x+i][y+j] += key[i][j]

                ### check에서 True가 나오면 True를 리턴하고 함수 종료
                if check(extended_lock) == True:
                    return True

                ### 다음 탐색을 위하여 extended lock을 원래대로 되돌림
                for i in range(m):
                    for j in range(m):
                        extended_lock[x+i][y+j] -= key[i][j]

    return False


if __name__ == '__main__':

    key = [[0,0,0],[1,0,0],[0,1,1]]
    lock = [[1,1,1],[1,1,0],[1,0,1]]

    print(solution(key,lock))