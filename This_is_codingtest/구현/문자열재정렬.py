import sys

sys.stdin = open("input.txt","r")

def resort(str_list):

    num = 0
    result = ''

    for strs in str_list:
        
        ###만약 string이 숫자 형태라면
        if strs.isdigit() == True:
            num += int(strs)
        else:
            result += strs

    ###알파벳들 다음에 숫자들을 더한 값을 추가
    result = result + str(num)

    return result

if __name__ =='__main__':

    S = sys.stdin.readline().strip()
    
    ###string을 알파벳 순으로 정렬
    sorted_s = sorted(S)
    
    print(resort(sorted_s))