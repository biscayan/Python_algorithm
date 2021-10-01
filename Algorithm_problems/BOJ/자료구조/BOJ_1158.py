N, K = map(int, input().split())
array = [i for i in range(1, N+1)]
sequence = []
idx = K-1
while array:
    idx %= len(array)
    sequence.append(array[idx])
    del array[idx]
    idx += K-1
print('<', end='')
for i in range(0, len(sequence)-1):
    print(f'{sequence[i]},', end=' ')
print(sequence[-1], end='')    
print('>')