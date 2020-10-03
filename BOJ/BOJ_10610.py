import sys

sys.stdin = open("input.txt", "r")

N = sys.stdin.readline()

N_list = list(N)

###큰수->작은수로 정렬
N_list.sort(reverse=True)
answer = ''

for num in N_list:
    answer += num

if "0" in N_list:
    if int(answer) % 3 == 0:
        print(int(answer))
    else:
        print(-1)
else:
    print(-1)