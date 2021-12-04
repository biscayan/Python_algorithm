import re
word = input()
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
for alpha in alphabets:
    if alpha in word:
        answer += word.count(alpha)
        word = re.sub(alpha,'0',word)
word = re.sub('0','',word)
answer += len(word)
print(answer)