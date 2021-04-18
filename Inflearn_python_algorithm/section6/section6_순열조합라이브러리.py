import itertools

n = 5

array = []

for i in range(1, n+1):
    array.append(i)

### 숫자 1~5까지의 순열
for per in itertools.permutations(array):
    print(per)

### 숫자 1~5까지에서 3개를 뽑아 만든 순열 
for per in itertools.permutations(array, 3):
    print(per)

### 숫자 1~5까지에서 3개를 뽑아 만든 조합
for com in itertools.combinations(array, 3):
    print(com)