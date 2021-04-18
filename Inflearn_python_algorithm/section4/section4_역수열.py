import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

reverse_seq = list(map(int,sys.stdin.readline().split()))

original_seq = [0] * N

for i in range(N):
    for j in range(N):
        if reverse_seq[i] == 0 and original_seq[j] ==0 :
            original_seq[j] = i+1
            break
        
        elif original_seq[j] == 0:
            reverse_seq[i] -= 1

print(' '.join(map(str,original_seq)))

            

    
