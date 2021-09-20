N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
for num in array:
    print(num)