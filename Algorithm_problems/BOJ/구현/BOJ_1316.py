import sys
import string

sys.stdin = open("input.txt", "r")

def group_word(word):

    global result

    ### 알파벳 체크할 딕셔너리 생성
    alphabet_dict = {}
    
    for alphabet in string.ascii_lowercase:
        alphabet_dict[alphabet] = 0
    
    alphabet_dict[word[0]] += 1

    for i in range(1, len(word)):
        
        ### 이전 알파벳과 다르다면 떨어져 나갔는지의 여부를 확인해봐야함
        if word[i] != word[i-1]:
            
            ### 알파벳이 이전에 등장한 적이 있다면 현재의 것은 떨어져 나간것임, 함수 종료
            if alphabet_dict[word[i]] != 0:
                return 

            else:
                alphabet_dict[word[i]] += 1

        else:
            alphabet_dict[word[i]] += 1
    
    ### 앞에서 함수가 종료되지 않았다면 그룹단어임, 따라서 result값을 +1
    result += 1

    return 


if __name__=='__main__':

    N = int(sys.stdin.readline())

    ### 결과를 담을 변수 생성, 전역변수로 사용 예정
    result = 0

    ### 체크할 단어 수 만큼 함수 호출
    for i in range(N):
        word = sys.stdin.readline().strip()
        group_word(word)

    print(result)