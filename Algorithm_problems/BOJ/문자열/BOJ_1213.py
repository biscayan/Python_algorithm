import sys
sys.stdin = open("input.txt", "r")

eng_name = sys.stdin.readline().strip()
ord_list = [0] * 26

for alpha in eng_name:
    ord_list[ord(alpha)-65] += 1

alphabet = ''
alpha_odd = ''
odd_cnt = 0

for i in range(26):
    if ord_list[i] % 2 == 1:
        alpha_odd += chr(i+65)
        odd_cnt += 1
    alphabet += (chr(i+65) * (ord_list[i] // 2))

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(alphabet+alpha_odd+alphabet[::-1])