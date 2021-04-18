import sys

sys.stdin = open("input.txt","r")

N = int(input())

word_dict = {}

for i in range(N):
    word = input()
    word_dict[word] = 0

for j in range(N-1):
    word2 = input()
    if word2 in word_dict:
        word_dict[word2] += 1

###출력방법1
for word in word_dict:
    if word_dict[word] == 0:
        print(word)
        break

###출력방법2
for key,val in word_dict.items():
    if val == 0:
        print(key)
        break