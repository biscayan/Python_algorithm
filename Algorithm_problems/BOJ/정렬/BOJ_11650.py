N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append((x,y))
array.sort(key = lambda tup:(tup[0],tup[1]))
for x,y in array:
    print(x,y)