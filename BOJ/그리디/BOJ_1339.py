import sys
import string

sys.stdin = open("input.txt","r")

def word_math(word_list):

    alphabet_dict = {}

    for alphabet in string.ascii_uppercase:
        alphabet_dict[alphabet] = 0

    for word in word_list:
        for i in range(len(word)):
            ###**의 연산속도가 pow()보다 빠름
            alphabet_dict[word[i]] += 10 ** (len(word)-i-1)

    ###value로 내림차순 정렬
    sorted_alpjabet_dict = sorted(alphabet_dict.items(), reverse=True, key = lambda item:item[1])

    result = 0
    weight = 9

    for alphabet_tuple in sorted_alpjabet_dict:

        value = alphabet_tuple[1]

        if value == 0:
            break

        result += value*weight
        weight -= 1

    print(result)


if __name__=='__main__':

    N = int(sys.stdin.readline())

    alphabet_list =  []

    for _ in range(N):
        ###strip으로 '\n'제거
        alphabets = sys.stdin.readline().strip()
        alphabet_list.append(alphabets)

    word_math(alphabet_list)