def solution(phone_book):
    answer=True

    #접두어를 찾기 위해 정렬
    phone_book=sorted(phone_book)

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer=False
            return answer
        else:
            return answer
            

if __name__=='__main__':
    #test case1
    phone_book=["119", "97674223", "1195524421"]
    print(solution(phone_book))

    #test case2
    phone_book=["123", "456", "789"]
    print(solution(phone_book))
    
    #test case3
    phone_book=["12", "123", "123", "1235", "567", "88"]
    print(solution(phone_book))
