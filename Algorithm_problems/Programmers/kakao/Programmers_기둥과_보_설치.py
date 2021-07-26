### 설치된 구조물이 가능한 것인지 체크
### 기둥 : (1) 바닥 위에 있거나 (2) 보의 한쪽 끝 부분 위에 있거나, (3) 다른 기둥 위에 있어야 합니다.
### 보 : (1) 한쪽 끝 부분이 기둥 위에 있거나 (2) 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def check(result):

    for frame in result:
        
        x, y, a = frame

        ### 기둥일때
        if a == 0:
            if y == 0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result:
                continue
            else:
                return False
        
        ### 보일때
        elif a == 1:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1]) in result:
                continue
            else:
                return False
    
    return True
    

def solution(n, build_frame):

    result = []

    for frame in build_frame:

        x, y, a, b = frame
        
        ### 삭제할때
        if b == 0:
            result.remove([x,y,a])
            ### 가능한 구조물이 아니라면 다시 설치
            if not check(result):
                result.append([x,y,a])

        ### 설치할때
        if b == 1:
            result.append([x,y,a])
            ### 가능한 구조물이 아니라면 삭제
            if not check(result):
                result.remove([x,y,a])

    result.sort()

    return result

if __name__ == '__main__':
    
    ### test case1
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))

    ### test case2
    n = 5
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(n, build_frame))