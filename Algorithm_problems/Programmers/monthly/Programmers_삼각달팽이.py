def solution(n):
    triangle = [[0 for j in range(i)] for i in range(1,n+1)]
    answer = []
    x,y = -1,0
    num = 1
    for r in range(n):
        for c in range(r,n):
            if r % 3 == 0:
                x += 1
            elif r % 3 == 1:
                y += 1
            elif r % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    for arr in triangle:
        answer.extend(arr)
    return answer